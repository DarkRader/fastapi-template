"""DTO schemes for UserLite entity."""

from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr, computed_field


class UserBase(BaseModel):
    """Shared properties of UserLite."""

    id: str
    username: str
    first_name: str
    second_name: str
    email: EmailStr


class UserCreate(UserBase):
    """Properties to receive via API on creation."""


class UserUpdate(BaseModel):
    """Properties to receive via API on update."""

    username: str | None = None
    first_name: str | None = None
    second_name: str | None = None
    email: EmailStr | None = None


class UserLite(UserBase):
    """Base model for user in database."""

    deleted_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True)

    @computed_field
    def full_name(self) -> str:
        return f"{self.first_name} {self.second_name}"


class UserDetail(UserLite):
    """Extended API response schema with events."""
