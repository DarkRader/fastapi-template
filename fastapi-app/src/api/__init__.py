"""Package for API modules."""

from api.dependencies import get_current_user
from api.v1 import router as router_v1
from fastapi import APIRouter

router = APIRouter()

router.include_router(router_v1)


__all__ = [
    "get_current_user",
    "router",
]
