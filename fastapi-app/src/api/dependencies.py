"""Module for authenticator functions."""

import logging
from typing import Annotated

from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from integrations.openid import OpenIDAuthService
from schemas import UserDetail
from services import UserService

logger = logging.getLogger(__name__)

http_bearer = HTTPBearer()


async def get_current_user(
    user_service: Annotated[UserService, Depends(UserService)],
    openid_service: Annotated[OpenIDAuthService, Depends(OpenIDAuthService)],
    token: Annotated[HTTPAuthorizationCredentials, Depends(http_bearer)],
) -> UserDetail:
    """
    Retrieve the current user based on a JWT token.

    :param user_service: UserLite service.
    :param openid_service: OpenID service.
    :param token: The authorization token.

    :return: User object.
    """
    logger.debug("Retrieving current user from token.")
    user_info = await openid_service.get_user_info(token)

    return await user_service.get(user_info.sub)
