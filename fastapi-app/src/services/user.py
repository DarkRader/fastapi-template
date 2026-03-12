"""
Define an abstract base class AbstractUserService.

This class works with User.
"""

import logging
from abc import ABC, abstractmethod

from core.application.exceptions import Entity, EntityNotFoundError
from core.dependencies.adapters import UserRepositoryDep
from core.ports.repositories import UserRepository
from schemas import (
    User,
    UserCreate,
    UserInfo,
    UserUpdate,
)
from services import CrudServiceBase

logger = logging.getLogger(__name__)


class AbstractUserService(
    CrudServiceBase[
        User,
        UserRepository,
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
    ) -> User:
        """
        Create a User in the database.

        :return: the created UserLite.
        """

    @abstractmethod
    async def get_by_username(self, username: str) -> User:
        """
        Retrieve a User instance by its username.

        :param username: The username of the UserLite.

        :return: The UserLite instance if found, None otherwise.
        """


class UserService(AbstractUserService):
    """Class UserService represent service that work with UserLite."""

    def __init__(
        self,
        user_repository: UserRepositoryDep,
    ) -> None:
        super().__init__(user_repository, Entity.USER)

    async def create_user(
        self,
        user_info: UserInfo,
    ) -> User:
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

    async def get_by_username(self, username: str) -> User:
        return await self.crud.get_by_username(username)
