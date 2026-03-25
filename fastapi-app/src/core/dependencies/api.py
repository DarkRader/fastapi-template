"""Dependencies for api layer."""

import logging
from collections.abc import Awaitable, Callable
from typing import Annotated

from core.application.exceptions import UnauthorizedError
from core.dependencies.services import UserServiceDep
from domain.schemas import User
from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from infrastructure.externals.openid_auth import OpenIdProvider

logger = logging.getLogger(__name__)

http_bearer = HTTPBearer()


async def get_current_user(
    service: UserServiceDep,
    openid_service: Annotated[OpenIdProvider, Depends(OpenIdProvider)],
    token: Annotated[HTTPAuthorizationCredentials, Depends(http_bearer)],
) -> User:
    """Retrieve the current user based on a JWT token."""
    logger.debug("Retrieving current user from token.")
    user_info = await openid_service.get_user_info(token)

    return await service.get_by_username(user_info.preferred_username)


CurrentUserDep = Annotated[User, Depends(get_current_user)]


def require_permissions(*permissions: str) -> Callable[..., Awaitable[User]]:
    """
    Create a dependency that ensures the current user has at least one of the given permissions.

    :param permissions: Allowed permissions for accessing the endpoint.
    :return: FastAPI dependency callable.
    """

    async def permissions_checker(
        user: CurrentUserDep,
    ) -> User:
        if not permissions:
            return user

        user_permissions = set(permissions)

        if not user_permissions.intersection(user):  # fix what check
            raise UnauthorizedError(
                message=f"Requires one of permissions: {permissions}",
            )

        return user

    return permissions_checker
