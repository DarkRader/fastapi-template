"""Defines the service for working with the Keycloak authorization."""

import logging
from abc import ABC, abstractmethod
from typing import Any

import aiohttp
import httpx
from authlib.integrations.starlette_client import OAuth
from authlib.jose import JsonWebToken
from core import settings
from core.application.exceptions import PermissionDeniedError, UnauthorizedError
from fastapi import status
from fastapi.security import HTTPAuthorizationCredentials
from schemas import UserInfo

log = logging.getLogger(__name__)


class AbstractOpenIDAuthService(ABC):
    """Interface for a service interacting with the OpenID Auth flow."""

    @abstractmethod
    async def decode_token(self, token: str) -> dict[str, Any]:
        """
        Decode an OpenID token.

        This method decodes the given token using OpenID provider's public key
        and ensures it is valid. If the token is invalid or expired,
        an HTTP 401 Unauthorized error is raised.

        :param token: The access token to decode.

        :return: A dictionary containing the decoded token information.
        """

    @abstractmethod
    async def get_user_info(self, token: HTTPAuthorizationCredentials) -> UserInfo:
        """
        Get user information from an access token.

        :param token: The access token.

        :return: A dictionary containing user profile information.
        """

    @abstractmethod
    async def logout(self, refresh_token: str) -> None:
        """
        Log out a user by invalidating their refresh token.

        :param refresh_token: The refresh token to invalidate.

        :return: None
        """


class OpenIDAuthService(AbstractOpenIDAuthService):
    """OpenID client for authentication operations."""

    def __init__(self) -> None:
        self.oauth = OAuth()
        self.oauth.register(
            name=settings.OPENID.CLIENT_NAME,
            client_id=settings.OPENID.CLIENT_ID,
            client_secret=settings.OPENID.CLIENT_SECRET,
            server_metadata_url=settings.OPENID.METADATA_URL,
            client_kwargs={"scope": " ".join(settings.OPENID.SCOPES)},
        )
        self.client = self.oauth.create_client(settings.OPENID.CLIENT_NAME)
        self.jwt = JsonWebToken(["RS256", "ES256", "HS256"])

    async def decode_token(self, token: str) -> dict[str, Any]:
        try:
            metadata = await self.client.load_server_metadata()
            jwks_uri = metadata["jwks_uri"]

            async with aiohttp.ClientSession() as session, session.get(jwks_uri) as resp:
                try:
                    jwks = await resp.json()
                except aiohttp.ContentTypeError as e:
                    text = await resp.text()
                    log.exception("JWKS endpoint returned non-JSON: %s", text)
                    msg = "Invalid JWKS response"
                    raise UnauthorizedError(msg) from e

            claims = self.jwt.decode(token, jwks)
            claims.validate()

            return dict(claims)

        except aiohttp.ClientError as e:
            log.info("Token decode failed (network error): %s", e)
            msg = "Unable to fetch JWKS"
            raise UnauthorizedError(msg) from e

        except Exception as e:
            log.info("Token decode failed: %s", e)
            msg = "Invalid or expired token"
            raise UnauthorizedError(msg) from e

    async def get_user_info(self, token: HTTPAuthorizationCredentials) -> UserInfo:
        token_dict = {"access_token": token.credentials, "token_type": token.scheme}

        try:
            resp = await self.client.userinfo(token=token_dict)
            return UserInfo(**resp)

        except httpx.HTTPStatusError as e:
            status_code = e.response.status_code

            if status_code == status.HTTP_401_UNAUTHORIZED:
                log.info("Invalid or expired token when calling userinfo: %s", e)
                msg = "Invalid or expired token"
                raise UnauthorizedError(message=msg) from e

            if status_code == status.HTTP_403_FORBIDDEN:
                log.info("Forbidden: token lacks permissions: %s", e)
                msg = "Token lacks required permissions"
                raise PermissionDeniedError(message=msg) from e

            log.exception("Unexpected HTTP error from userinfo: %s")
            msg = "OIDC provider rejected the request"
            raise UnauthorizedError(message=msg) from e

        except httpx.RequestError as e:
            log.exception("Network error when contacting OIDC provider: %s")
            msg = "OIDC provider unreachable"
            raise UnauthorizedError(message=msg) from e

        except Exception as e:
            log.exception("Unexpected error during OIDC userinfo")
            msg = "Failed to retrieve user info"
            raise UnauthorizedError(message=msg) from e

    async def logout(self, refresh_token: str) -> None:
        try:
            metadata = await self.client.load_server_metadata()
            logout_url = metadata.get("end_session_endpoint")
            if not logout_url:
                log.warning("No end_session_endpoint configured in metadata")
                return

            async with (
                aiohttp.ClientSession() as session,
                session.post(
                    logout_url,
                    data={
                        "client_id": settings.OPENID.CLIENT_ID,
                        "client_secret": settings.OPENID.CLIENT_SECRET,
                        "refresh_token": refresh_token,
                    },
                ) as resp,
            ):
                try:
                    data = await resp.json()
                except aiohttp.ContentTypeError:
                    data = await resp.text()

                log.info("OIDC logout response (%s): %s", resp.status, data)

                if resp.status == status.HTTP_401_UNAUTHORIZED:
                    msg = "Invalid or missing credentials for logout."
                    raise UnauthorizedError(msg)
                if resp.status == status.HTTP_400_BAD_REQUEST:
                    msg = f"Bad request during logout: {data['error_description']}"
                    raise UnauthorizedError(msg)
                if resp.status != status.HTTP_204_NO_CONTENT:
                    msg = "Unexpected error during logout"
                    raise PermissionDeniedError(msg)

                log.info("Logout successful")

        except aiohttp.ClientError as e:
            log.exception("Network error when contacting OIDC provider: %s")
            msg = "Failed to connect to OIDC provider"
            raise UnauthorizedError(msg) from e
