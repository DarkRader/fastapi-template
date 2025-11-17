"""API controllers for authorisation in IS(Information System of the club)."""

import logging
from typing import Annotated

from core import settings
from core.application.exceptions import ERROR_RESPONSES
from fastapi import APIRouter, Body, Depends, FastAPI, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer, OAuth2AuthorizationCodeBearer
from integrations.openid import OpenIDAuthService
from schemas import UserDetail
from services import UserService

log = logging.getLogger(__name__)

app = FastAPI()

router = APIRouter()


http_bearer = HTTPBearer()


oauth2_scheme = OAuth2AuthorizationCodeBearer(
    authorizationUrl=settings.OPENID.AUTH_URL,
    tokenUrl=settings.OPENID.TOKEN_URL,
)


@router.get(
    "/token-swagger",
    status_code=status.HTTP_200_OK,
)
async def get_token(token: Annotated[str, Depends(oauth2_scheme)]) -> dict:
    """
    Retrieve the OAuth2 access token from the authorization code flow.

    This endpoint is intended for use with Swagger UI. When a user
    authenticates via Keycloak through the Swagger interface,
    FastAPI's `OAuth2AuthorizationCodeBearer` dependency automatically
    handles the OAuth2 code exchange and injects the resulting access token.
    """
    return {"access_token": token}


@router.post(
    "/login",
    responses=ERROR_RESPONSES["401"],
    status_code=status.HTTP_200_OK,
)
async def login(
    user_service: Annotated[UserService, Depends(UserService)],
    openid_service: Annotated[OpenIDAuthService, Depends(OpenIDAuthService)],
    token: Annotated[HTTPAuthorizationCredentials, Depends(http_bearer)],
) -> UserDetail:
    """Authenticate a user."""
    log.info("Login attempt started with bearer token.")
    user_info = await openid_service.get_user_info(token)
    user = await user_service.create_user(user_info)
    log.info("User %s successfully authenticated and synced.", user.id)

    return user


@router.post(
    "/logout",
    responses=ERROR_RESPONSES["400_401"],
    status_code=status.HTTP_204_NO_CONTENT,
)
async def logout(
    openid_service: Annotated[OpenIDAuthService, Depends(OpenIDAuthService)],
    refresh_token: Annotated[str, Body()],
) -> None:
    """Clean session of the current user."""
    await openid_service.logout(refresh_token)
