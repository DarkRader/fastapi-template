"""
SQLAlchemy adapter for UserRepository port.

Implements the UserRepository interface using SQLAlchemy to interact
with the UserModel table asynchronously. All service operations
depend on UserRepository, not this concrete class.
"""

from core.ports.repositories.user import UserRepository
from infrastructure.db.repositories.base import SQLAlchemyCRUDBase
from models import UserModel
from schemas import UserCreate, UserUpdate
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


class SQLAlchemyUserRepository(
    SQLAlchemyCRUDBase[UserModel, UserCreate, UserUpdate], UserRepository
):
    """Adapter implementing UserRepository with SQLAlchemy."""

    def __init__(self, db: AsyncSession) -> None:
        super().__init__(UserModel, db)

    async def get_by_username(self, username: str) -> UserModel | None:
        stmt = select(self.model).filter(self.model.username == username)
        result = await self.db.execute(stmt)
        return result.scalar_one_or_none()
