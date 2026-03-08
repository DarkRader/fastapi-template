"""Database repository ports for domain models."""

from core.ports.repositories.base import CRUDBase
from core.ports.repositories.user import UserRepository

__all__ = [
    "CRUDBase",
    "UserRepository",
]
