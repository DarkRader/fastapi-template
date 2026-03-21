"""Shortcuts to easily import schemes."""

from domain.schemas.base import Pagination
from domain.schemas.openid import UserInfo
from domain.schemas.user import User, UserCreate, UserUpdate
from domain.schemas.well_known import WellKnownResponse

__all__ = [
    "Pagination",
    "User",
    "UserCreate",
    "UserInfo",
    "UserUpdate",
    "WellKnownResponse",
]
