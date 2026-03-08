"""API controllers for users."""

import logging

from core.application.exceptions import (
    ERROR_RESPONSES,
)
from core.dependencies.api import CurrentUserDep
from core.dependencies.services import UserServiceDep
from fastapi import APIRouter, status
from schemas import UserDetail, UserLite

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get(
    "/",
    responses=ERROR_RESPONSES["401_403"],
    status_code=status.HTTP_200_OK,
)
async def get_all(
    service: UserServiceDep,
    user: CurrentUserDep,
) -> list[UserLite]:
    """
    Retrieve all users from the database.

    This endpoint is accessible only to users with the 'section_head' role.
    It returns a list of all registered users.
    """
    logger.info("User %s requested list of all users.", user.username)

    users = await service.get_all()

    logger.info("Returned %d users for section head %s.", len(users), user.username)
    return users


@router.get(
    "/me",
    responses=ERROR_RESPONSES["401"],
    status_code=status.HTTP_200_OK,
)
async def get_me(
    user: UserServiceDep,
) -> UserDetail:
    """Get currently authenticated user."""
    logger.debug("Returning profile for user %s.", user.username)
    return user
