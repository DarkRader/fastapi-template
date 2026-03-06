"""Provide CRUD repositories for each domain model to handle database operations."""

from .base import CRUDBase
from .user import CRUDUser

__all__ = [
    "CRUDBase",
    "CRUDUser",
]
