"""Base DTO schemas for data returned from the API."""

from typing import TypeVar

from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)


class Pagination[T: BaseModel](BaseModel):
    """Base DTO containing pagination metadata."""

    items: list[T]
    skip: int
    limit: int
    total: int
    has_previous: bool
    has_next: bool
