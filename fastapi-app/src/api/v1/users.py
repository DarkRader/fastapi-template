"""API controllers for users."""

import logging
from typing import Annotated

from core.application.exceptions import (
    ERROR_RESPONSES,
)
from core.dependencies.api import CurrentUserDep
from core.dependencies.services import UserServiceDep
from fastapi import APIRouter, Query, status
from schemas import Pagination, User

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get(
    "/",
    responses=ERROR_RESPONSES["401_403"],
    status_code=status.HTTP_200_OK,
)
async def get_list(
    service: UserServiceDep,
    user: CurrentUserDep,
    *,
    skip: Annotated[int, Query(ge=0, description="Number of records to skip (offset).")] = 0,
    limit: Annotated[
        int, Query(ge=1, le=100, description="Maximum number of records to return.")
    ] = 10,
    include_removed: Annotated[bool, Query(description="Include removed objects.")] = False,
) -> Pagination[User]:
    """
    Retrieve all users from the database.

    It returns a list of registered users.
    """
    logger.info("User %s requested list of users.", user.username)

    users = await service.get_list(skip, limit, include_removed=include_removed)

    logger.info("Returned users list for user %s.", user.username)
    return users


@router.get(
    "/me",
    responses=ERROR_RESPONSES["401"],
    status_code=status.HTTP_200_OK,
)
async def get_me(
    user: CurrentUserDep,
) -> User:
    """Get currently authenticated user."""
    logger.debug("Returning profile for user %s.", user.username)
    return user
