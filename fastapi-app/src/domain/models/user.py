"""User ORM model and its dependencies."""

from domain.models.base_class import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column


class User(Base):
    """User model to create and manipulate user entity in the database."""

    provider_id: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    second_name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)

    @property
    def full_name(self) -> str:
        """Return the user's full name composed of first and second names."""
        return f"{self.first_name} {self.second_name}"
