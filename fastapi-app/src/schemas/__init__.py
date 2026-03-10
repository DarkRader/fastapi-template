"""Shortcuts to easily import schemes."""

from .base import Pagination
from .openid import UserInfo
from .user import UserCreate, UserDetail, UserLite, UserUpdate
from .well_known import WellKnownResponse

__all__ = [
    "Pagination",
    "UserCreate",
    "UserDetail",
    "UserInfo",
    "UserLite",
    "UserUpdate",
    "WellKnownResponse",
]
