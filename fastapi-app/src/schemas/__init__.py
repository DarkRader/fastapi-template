"""Shortcuts to easily import schemes."""

from .openid import UserInfo
from .user import UserCreate, UserDetail, UserLite, UserUpdate

__all__ = [
    "UserCreate",
    "UserDetail",
    "UserInfo",
    "UserLite",
    "UserUpdate",
]
