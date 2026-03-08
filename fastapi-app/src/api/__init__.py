"""Package for API modules."""

from api.v1 import router as router_v1
from api.well_known import router as router_well_known
from core.application.docs import fastapi_docs
from fastapi import APIRouter

router = APIRouter()

router.include_router(
    router_well_known,
    prefix="/well-known",
    tags=[fastapi_docs.WELL_KNOWN_TAG["name"]],
)

router.include_router(router_v1)


__all__ = [
    "APIRouter",
    "fastapi_docs",
    "router_v1",
    "router_well_known",
]
