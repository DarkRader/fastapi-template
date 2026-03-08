"""Dependencies for adapters."""

from typing import Annotated

from core.db import AsyncSessionDep
from core.ports.repositories.user import UserRepository
from fastapi import Depends
from infrastructure.db.repositories.user import SQLAlchemyUserRepository
from infrastructure.externals.openid_auth import OpenIdProvider

# REPOSITORIES DEPENDENCIES


def get_user_repository(
    db: AsyncSessionDep,
) -> UserRepository:
    """Get User Service."""
    return SQLAlchemyUserRepository(db)


UserRepositoryDep = Annotated[UserRepository, Depends(get_user_repository)]


def get_openid_provider() -> OpenIdProvider:
    """Get User Service."""
    return OpenIdProvider()


OpenIdProvider = Annotated[OpenIdProvider, Depends(get_openid_provider)]
