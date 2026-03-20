"""
Port interface for CRUD operations on User entities.

This interface extends the generic CRUDBase port and defines
additional contract methods specific to the User domain.

Concrete implementations (adapters) should handle all database
interactions for UserModel while adhering to this interface.
"""

from abc import ABC, abstractmethod

from core.ports.repositories.base import CRUDBase
from domain.models import UserModel
from domain.schemas import UserCreate, UserUpdate


class UserRepository(CRUDBase[UserModel, UserCreate, UserUpdate], ABC):
    """Repository port defining CRUD operations and queries for User entities."""

    @abstractmethod
    async def get_by_username(self, username: str) -> UserModel | None:
        """
        Retrieve a User instance by its username.

        :param username: The username of the User.

        :return: The User instance if found, None otherwise.
        """
