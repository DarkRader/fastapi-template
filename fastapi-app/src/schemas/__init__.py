"""Shortcuts to easily import schemes."""

from .base import Pagination
from .openid import UserInfo
from .user import User, UserCreate, UserUpdate
from .well_known import WellKnownResponse

__all__ = [
    "Pagination",
    "User",
    "UserCreate",
    "UserInfo",
    "UserUpdate",
    "WellKnownResponse",
]
