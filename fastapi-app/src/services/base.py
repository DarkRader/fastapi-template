"""
Ports and base services for CRUD operations.

This module defines abstract service interfaces (ports) and a generic base
implementation for services that operate on domain models using CRUD repositories.

It separates the service layer from the database implementation, allowing
dependency inversion and easy substitution of concrete repositories.
"""

from abc import ABC, abstractmethod
from typing import TypeVar

from core.application.exceptions import BaseAppError, Entity, EntityNotFoundError
from core.ports.repositories import CRUDBase
from pydantic import BaseModel
from schemas import Pagination

Schema = TypeVar("Schema", bound=BaseModel)
Crud = TypeVar("Crud", bound=CRUDBase)
CreateSchema = TypeVar("CreateSchema", bound=BaseModel)
UpdateSchema = TypeVar("UpdateSchema", bound=BaseModel)


class AbstractCRUDService[
    Schema: BaseModel,
    Crud: CRUDBase,
    CreateSchema: BaseModel,
    UpdateSchema: BaseModel,
](ABC):
    """
    Service port defining the interface for CRUD operations.

    This is an abstract interface (port) for any service that manages
    domain entities via a CRUD repository. It ensures that all services
    expose a consistent set of operations without binding to a specific
    database implementation.
    """

    @abstractmethod
    async def get(
        self,
        id_: str,
        *,
        include_removed: bool = False,
    ) -> Schema:
        """
        Retrieve an object from the database.

        If include_removed is True retrieve a single record
        including marked as deleted.

        :param id_: the ID of the object to retrieve.
        :param include_removed: include removed object or not.

        :returns T: the retrieved object.
        """

    @abstractmethod
    async def get_list(
        self, skip: int = 0, limit: int = 10, *, include_removed: bool = False
    ) -> Pagination[Schema]:
        """
        Retrieve a paginated list of objects from the database.

        :param skip: Number of records to skip (offset).
        :param limit: Maximum number of records to return.
        :param include_removed: include removed object or not.

        :returns: A list of objects for the requested page.
        """

    @abstractmethod
    async def get_all(self, *, include_removed: bool = False) -> list[Schema]:
        """
        Retrieve all objects from the database.

        If include_removed is True retrieve all objects
        including marked as deleted.

        :param include_removed: include removed object or not.

        :returns List[T]: A list of all objects in the database.
        """

    @abstractmethod
    async def create(self, obj_in: CreateSchema) -> Schema:
        """
        Create an object in the database.

        :param obj_in: the object to create.

        :returns T: the created object.
        """

    @abstractmethod
    async def update(
        self,
        id_: str,
        obj_in: UpdateSchema,
    ) -> Schema:
        """
        Update an object in the database.

        :param id_: the ID of the object to update.
        :param obj_in: the updated object.

        :returns T: the updated object.
        """

    @abstractmethod
    async def restore(self, id_: str) -> Schema:
        """
        Restore a previously soft-removed object by its ID.

        :param id_: The ID of the object to restore.

        :returns T: The restored object.
        """

    @abstractmethod
    async def delete(self, id_: str, *, hard_remove: bool = False) -> Schema:
        """
        Delete an object from the database.

        :param id_: The ID of the object to delete.
        :param hard_remove: hard remove the object or not.
        """


class CrudServiceBase(AbstractCRUDService[Schema, Crud, CreateSchema, UpdateSchema]):
    """
    Generic base service implementing CRUD operations.

    This base class implements the AbstractCRUDService interface using
    a CRUD repository. It provides default behavior for creating, reading,
    updating, soft-deleting, restoring, and hard-deleting entities.

    Subclasses can extend this class to add domain-specific logic while
    reusing standard CRUD behavior.
    """

    def __init__(self, crud: Crud, entity_name: Entity) -> None:
        self.crud: Crud = crud
        self.entity_name: Entity = entity_name

    async def get(
        self,
        id_: str,
        *,
        include_removed: bool = False,
    ) -> Schema:
        obj = await self.crud.get(id_, include_removed=include_removed)
        if obj is None:
            raise EntityNotFoundError(self.entity_name, id_)
        return obj

    async def get_list(
        self, skip: int = 0, limit: int = 10, *, include_removed: bool = False
    ) -> Pagination[Schema]:
        items = await self.crud.get_list(skip=skip, limit=limit, include_removed=include_removed)
        total = await self.crud.count(include_removed=include_removed)
        return {
            "items": items,
            "skip": skip,
            "limit": limit,
            "total": total,
            "has_previous": skip > 0,
            "has_next": skip + limit < total,
        }

    async def get_all(self, *, include_removed: bool = False) -> list[Schema]:
        return await self.crud.get_all(include_removed=include_removed)

    async def create(self, obj_in: CreateSchema) -> Schema:
        return await self.crud.create(obj_in)

    async def update(
        self,
        id_: str,
        obj_in: UpdateSchema,
    ) -> Schema:
        obj_to_update = await self.get(id_)
        if obj_to_update is None:
            raise EntityNotFoundError(self.entity_name, id_)
        return await self.crud.update(db_obj=obj_to_update, obj_in=obj_in)

    async def restore(self, id_: str) -> Schema:
        obj = await self.get(id_, include_removed=True)
        if obj.deleted_at is None:  # type: ignore[attr-defined]
            msg = f"A {self.entity_name.value} was not soft deleted."
            raise BaseAppError(msg)
        if obj is None:
            raise EntityNotFoundError(self.entity_name, id_)
        return await self.crud.restore(obj)

    async def delete(self, id_: str, *, hard_remove: bool = False) -> Schema:
        obj = await self.get(id_, include_removed=True)
        if hard_remove:
            return await self.crud.remove(id_)
        if obj.deleted_at is not None:  # type: ignore[attr-defined]
            msg = f"A {self.entity_name.value} is already soft deleted."
            raise BaseAppError(msg)
        return await self.crud.soft_remove(obj)
