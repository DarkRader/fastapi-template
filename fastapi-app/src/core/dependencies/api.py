"""Dependencies for api layer."""

import logging
from typing import Annotated

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
