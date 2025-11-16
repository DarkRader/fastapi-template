"""API router for v2 of the Reservation System."""

from api.v1.auth import router as auth_router
from api.v1.users import router as users_router
from core.application.docs import fastapi_docs
from fastapi import APIRouter

router = APIRouter(
    prefix="/v2",
)

router.include_router(
    auth_router,
    prefix="/auth",
    tags=[fastapi_docs.AUTHORISATION_TAG["name"]],
)

router.include_router(
    users_router,
    prefix="/users",
    tags=[fastapi_docs.USER_TAG["name"]],
)
