"""
Port interface for generic CRUD operations on database models.

Concrete adapters, such as SQLAlchemy or other ORMs, should implement
this interface and handle actual database interactions.
"""

from abc import ABC, abstractmethod
from typing import TypeVar

from models.base_class import Base
from pydantic import BaseModel

Model = TypeVar("Model", bound=Base)
CreateSchema = TypeVar("CreateSchema", bound=BaseModel)
UpdateSchema = TypeVar("UpdateSchema", bound=BaseModel)


class CRUDBase[Model, CreateSchema, UpdateSchema](ABC):
    """Repository port defining standard CRUD operations for a model."""

    @abstractmethod
    async def get(
        self,
        id_: str,
        *,
        include_removed: bool = False,
    ) -> Model | None:
        """
        Retrieve a single record by its id_.

        If include_removed is True retrieve a single record
        including marked as deleted.
        """

    @abstractmethod
    async def get_multi(self, skip: int = 0, limit: int = 100) -> list[Model]:
        """Retrieve a list of records with pagination."""

    @abstractmethod
    async def get_all(self, *, include_removed: bool = False) -> list[Model]:
        """
        Retrieve all records without pagination.

        If include_removed is True retrieve all records
        including marked as deleted.
        """

    @abstractmethod
    async def create(self, obj_in: CreateSchema) -> Model:
        """Create a new record from the input scheme."""

    @abstractmethod
    async def update(
        self,
        *,
        db_obj: Model,
        obj_in: UpdateSchema,
    ) -> Model | None:
        """Update an existing record with the input scheme."""

    @abstractmethod
    async def restore(
        self,
        obj: Model,
    ) -> Model:
        """Retrieve removed object from soft removed."""

    @abstractmethod
    async def remove(self, id_: str | int) -> Model:
        """Remove a record by its id_."""

    @abstractmethod
    async def soft_remove(self, obj: Model) -> Model:
        """
        Soft remove a record by its id_.

        Change attribute deleted_at to time of deletion
        """
