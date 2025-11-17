"""App factory module for the FastAPI application."""

import logging
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from core.config import settings
from core.db import db_session
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from starlette.middleware.cors import CORSMiddleware

log = logging.getLogger(__name__)


@asynccontextmanager
async def startup_event(fast_api_app: FastAPI) -> AsyncGenerator[None, None]:  # noqa: ARG001
    """
    Startup and shutdown lifecycle event handler.

    This function is triggered when the FastAPI app starts and stops.
    It logs startup and shutdown messages.

    :param fast_api_app: The FastAPI application instance.
    """
    log.info("Starting %s.", settings.APP_NAME)
    yield
    await db_session.dispose()
    log.info("Shutting down %s.", settings.APP_NAME)


def create_app() -> FastAPI:
    """
    Create and configure the FastAPI app.

    This sets up:
    - Application metadata
    - Routers for API modules
    - Custom exception handler
    - Middleware (sessions, CORS)

    :return: A fully configured FastAPI app instance.
    """
    # Local imports to avoid circular import
    from api.routers import router  # noqa: PLC0415
    from core.application.docs import fastapi_docs  # noqa: PLC0415
    from core.application.exceptions import register_errors_handlers  # noqa: PLC0415

    app = FastAPI(
        title=fastapi_docs.NAME,
        description=fastapi_docs.DESCRIPTION,
        version=fastapi_docs.VERSION,
        openapi_tags=fastapi_docs.get_tags_metadata(),
        lifespan=startup_event,
        default_response_class=ORJSONResponse,
    )

    app.include_router(router)

    register_errors_handlers(app)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            "http://localhost:3000",
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app
