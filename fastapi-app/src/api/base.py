"""Base module for generating CRUD routes in FastAPI."""

import logging
from collections.abc import Callable
from typing import Annotated, TypeVar

from core.application.exceptions import ERROR_RESPONSES, Entity
from core.dependencies.api import require_permissions
from domain.schemas import Pagination
from fastapi import APIRouter, Depends, Path, Query, status
from pydantic import UUID7, BaseModel
from services.base import CrudServiceBase

logger = logging.getLogger(__name__)

TCreate = TypeVar("TCreate", bound=BaseModel)
TUpdate = TypeVar("TUpdate", bound=BaseModel)
TRead = TypeVar("TRead", bound=BaseModel)
TService = TypeVar("TService", bound=CrudServiceBase)


# ruff: noqa: PLR0913
class BaseCRUDRouter[
    TCreate: BaseModel,
    TUpdate: BaseModel,
    TRead: BaseModel,
    TService: CrudServiceBase,
]:
    """
    A base class for automatically registering standard CRUD routes to a FastAPI router.

    This router builder registers endpoints for:
    - GET all
    - GET by ID
    - POST (create)
    - PUT (update)
    - DELETE

    You can selectively disable/enable each operation using the corresponding flags.

    :param router: FastAPI APIRouter instance.
    :param service_dep: Dependency-injected service providing business logic.
    :param schema_create: Pydantic schema used for creating the resource.
    :param schema_update: Pydantic schema used for updating the resource.
    :param schema: Pydantic schema used for reading the resource.
    :param entity_name: A human-readable name for the entity (used in error messages).
    :param enable_create: Whether to register the create endpoint.
    :param enable_read: Whether to register the read (get) endpoints.
    :param enable_update: Whether to register the update endpoint.
    :param enable_delete: Whether to register the delete endpoint.
    """

    def __init__(
        self,
        router: APIRouter,
        *,
        service_dep: Callable[..., TService],
        schema_create: type[TCreate],
        schema_update: type[TUpdate],
        schema: type[TRead],
        entity_name: Entity,
        enable_create: bool = True,
        enable_read: bool = True,
        enable_read_all: bool = True,
        enable_create_multiple: bool = True,
        enable_update: bool = True,
        enable_restore: bool = True,
        enable_delete: bool = True,
        permissions_read: tuple[str, ...] = (),
        permissions_create: tuple[str, ...] = (),
        permissions_update: tuple[str, ...] = (),
        permissions_delete: tuple[str, ...] = (),
        permissions_restore: tuple[str, ...] = (),
    ) -> None:
        self.router = router
        self.entity_name = entity_name
        self.service_dep = service_dep

        # Schemas
        self.schema_create = schema_create
        self.schema_update = schema_update
        self.schema = schema

        # route toggles
        self.enable_create = enable_create
        self.enable_create_multiple = enable_create_multiple
        self.enable_read = enable_read
        self.enable_read_all = enable_read_all
        self.enable_update = enable_update
        self.enable_restore = enable_restore
        self.enable_delete = enable_delete

        # Roles list
        self.permissions_read = permissions_read
        self.permissions_create = permissions_create
        self.permissions_update = permissions_update
        self.permissions_delete = permissions_delete
        self.permissions_restore = permissions_restore

        self._ROUTES = [
            ("enable_read_all", self.register_get_all),
            ("enable_read", self.register_get_by_id),
            ("enable_create", self.register_create),
            ("enable_create_multiple", self.register_create_multiple),
            ("enable_update", self.register_update),
            ("enable_restore", self.register_restore),
            ("enable_delete", self.register_delete),
        ]

    # ---------- registration ----------
    def register_routes(self) -> None:
        """Register all enabled routes according to builder flags."""
        for flag, register_fn in self._ROUTES:
            if getattr(self, flag, False):
                register_fn()

    # ---------- route registrations ----------
    def register_get_all(self) -> None:
        """Register the GET / endpoint to retrieve all entities."""
        service_dep: Callable[..., TService] = self.service_dep

        @self.router.get(
            "/",
            dependencies=[Depends(require_permissions(*self.permissions_read))],
            status_code=status.HTTP_200_OK,
        )
        async def get_list(
            service: Annotated[TService, Depends(service_dep)],
            *,
            skip: Annotated[
                int, Query(ge=0, description="Number of records to skip (offset).")
            ] = 0,
            limit: Annotated[
                int, Query(ge=1, le=100, description="Maximum number of records to return.")
            ] = 10,
            include_removed: Annotated[bool, Query(description="Include removed objects.")] = False,
        ) -> Pagination[TRead]:
            """Get all objects."""
            logger.info(
                "Fetching list of %s (include_removed=%s)", self.entity_name.value, include_removed
            )
            result = await service.get_list(skip, limit, include_removed=include_removed)
            logger.debug("Fetched %d objects", len(result.items))
            return result

    def register_get_by_id(self) -> None:
        """Register the GET /{id} endpoint to retrieve an entity by its ID."""
        service_dep: Callable[..., TService] = self.service_dep

        @self.router.get(
            "/{id}",
            response_model=self.schema,
            dependencies=[Depends(require_permissions(*self.permissions_read))],
            responses=ERROR_RESPONSES["404"],
            status_code=status.HTTP_200_OK,
        )
        async def get_by_id(
            service: Annotated[TService, Depends(service_dep)],
            id_: Annotated[UUID7, Path(alias="id", description="The ID of the object.")],
            *,
            include_removed: Annotated[bool, Query(description="Include removed objects.")] = False,
        ) -> TRead:
            """Get object."""
            logger.info(
                "Fetching %s by id=%s (include_removed=%s)",
                self.entity_name.value,
                id_,
                include_removed,
            )
            obj = await service.get(id_, include_removed=include_removed)
            logger.debug("Fetched %s: %s", self.entity_name.value, obj)
            return obj

    def register_create(self) -> None:
        """Register the POST / endpoint to create a new entity."""
        service_dep: Callable[..., TService] = self.service_dep

        @self.router.post(
            "/",
            response_model=self.schema,
            dependencies=[Depends(require_permissions(*self.permissions_create))],
            responses=ERROR_RESPONSES["400_401_403_409"],
            status_code=status.HTTP_201_CREATED,
        )
        async def create(
            service: Annotated[TService, Depends(service_dep)],
            obj_create: TCreate,
        ) -> TRead:
            """Create object, only users with special roles can create object."""
            obj = await service.create(obj_create)
            logger.debug("Created %s: %s", self.entity_name.value, obj)
            return obj

    def register_create_multiple(self) -> None:
        """Register the POST / endpoint to create multiple entities."""
        service_dep: Callable[..., TService] = self.service_dep

        @self.router.post(
            "/batch",
            dependencies=[Depends(require_permissions(*self.permissions_create))],
            responses=ERROR_RESPONSES["400_401_403_409"],
            status_code=status.HTTP_201_CREATED,
        )
        async def create_multiple(
            service: Annotated[TService, Depends(service_dep)],
            objs_create: list[TCreate],
        ) -> list[TRead]:
            """Create multiple objects in a single request."""
            objs_result = await service.create_bulk(objs_create)
            logger.debug("Created multiple %s: %s", self.entity_name.value, objs_result)
            return objs_result

    def register_update(self) -> None:
        """Register the PUT /{id} endpoint to update an existing entity."""
        service_dep: Callable[..., TService] = self.service_dep

        @self.router.put(
            "/{id}",
            response_model=self.schema,
            dependencies=[Depends(require_permissions(*self.permissions_update))],
            responses=ERROR_RESPONSES["400_401_403_404"],
            status_code=status.HTTP_200_OK,
        )
        async def update(
            service: Annotated[TService, Depends(service_dep)],
            id_: Annotated[UUID7, Path(alias="id", description="The ID of the object.")],
            obj_update: TUpdate,
        ) -> TRead:
            """Update object, only users with special roles can update object."""
            obj = await service.update(id_, obj_update)
            logger.debug("Updated %s: %s", self.entity_name.value, obj)
            return obj

    def register_restore(self) -> None:
        """Register the PUT /{id}/restore endpoint to restore soft delete entity."""
        service_dep: Callable[..., TService] = self.service_dep

        @self.router.put(
            "/{id}/restore",
            response_model=self.schema,
            dependencies=[Depends(require_permissions(*self.permissions_restore))],
            responses=ERROR_RESPONSES["400_401_403_404"],
            status_code=status.HTTP_200_OK,
        )
        async def restore(
            service: Annotated[TService, Depends(service_dep)],
            id_: Annotated[UUID7, Path(alias="id", description="The ID of the object.")],
        ) -> TRead:
            """Restore a soft-deleted object, only users with special roles can restore object."""
            obj = await service.restore(id_)
            logger.debug("Restored object: %s", obj)
            return obj

    def register_delete(self) -> None:
        """Register the DELETE /{id} endpoint to delete an entity."""
        service_dep: Callable[..., TService] = self.service_dep

        @self.router.delete(
            "/{id}",
            response_model=self.schema,
            dependencies=[Depends(require_permissions(*self.permissions_delete))],
            responses=ERROR_RESPONSES["400_401_403_404"],
            status_code=status.HTTP_200_OK,
        )
        async def delete(
            service: Annotated[TService, Depends(service_dep)],
            id_: Annotated[UUID7, Path(alias="id", description="The ID of the object.")],
            *,
            hard_remove: Annotated[
                bool, Query(description="`Hard remove` the object or not.")
            ] = False,
        ) -> TRead:
            """Delete object, only users with special roles can delete object."""
            obj = await service.delete(id_, hard_remove=hard_remove)
            logger.debug("Deleted object: %s", obj)
            return obj
