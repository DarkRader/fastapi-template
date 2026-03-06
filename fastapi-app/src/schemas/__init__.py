"""Shortcuts to easily import schemes."""

from .openid import UserInfo
from .user import UserCreate, UserDetail, UserLite, UserUpdate
from .well_known import WellKnownResponse

__all__ = [
    "UserCreate",
    "UserDetail",
    "UserInfo",
    "UserLite",
    "UserUpdate",
    "WellKnownResponse",
]
