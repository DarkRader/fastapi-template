"""DTO schemes for Well Known responce entity."""
from pydantic import BaseModel, Field


class WellKnownResponse(BaseModel):
    """Well Known Response schema."""

    status: str = Field(..., example="Ok")
