"""Dependencies for services."""

from typing import Annotated

from core.dependencies.adapters import UserRepositoryDep
from fastapi import Depends
from services.user import UserService


def get_user_service(
    user_repository: UserRepositoryDep,
) -> UserService:
    """Get User Service."""
    return UserService(user_repository)


UserServiceDep = Annotated[UserService, Depends(get_user_service)]
