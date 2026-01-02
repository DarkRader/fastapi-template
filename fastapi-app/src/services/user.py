"""
Define an abstract base class AbstractUserService.

This class works with User.
"""

import logging
from abc import ABC, abstractmethod
from typing import Annotated

from core.application.exceptions import Entity, EntityNotFoundError
from core.db import db_session
from crud import CRUDUser
from fastapi import Depends
from schemas import (
    UserCreate,
    UserDetail,
    UserInfo,
    UserLite,
    UserUpdate,
)
from services import CrudServiceBase
from sqlalchemy.ext.asyncio import AsyncSession

logger = logging.getLogger(__name__)


class AbstractUserService(
    CrudServiceBase[
        UserLite,
        UserDetail,
        CRUDUser,
        UserCreate,
        UserUpdate,
    ],
    ABC,
):
    """
    Abstract class defines the interface for a user service.

    Provides CRUD operations for a specific UserModel.
    """

    @abstractmethod
    async def create_user(
        self,
        user_info: UserInfo,
    ) -> UserLite:
        """
        Create a User in the database.

        :return: the created UserLite.
        """

    @abstractmethod
    async def get_by_username(self, username: str) -> UserLite:
        """
        Retrieve a User instance by its username.

        :param username: The username of the UserLite.

        :return: The UserLite instance if found, None otherwise.
        """


class UserService(AbstractUserService):
    """Class UserService represent service that work with UserLite."""

    def __init__(
        self,
        db: Annotated[AsyncSession, Depends(db_session.session_getter)],
    ) -> None:
        super().__init__(CRUDUser(db), Entity.USER)

    async def create_user(
        self,
        user_info: UserInfo,
    ) -> UserDetail:
        try:
            user = await self.get(user_info.sub)
        except EntityNotFoundError:
            user = None
            logger.info("User with sub %s not found, creating in db.", user_info.sub)

        if not user:
            user_create = UserCreate(
                id=user_info.sub,
                username=user_info.preferred_username,
                first_name=user_info.given_name,
                second_name=user_info.family_name,
                email=user_info.email,
            )
            return await self.crud.create(user_create)
        return user

    async def get_by_username(self, username: str) -> UserDetail:
        return await self.crud.get_by_username(username)
