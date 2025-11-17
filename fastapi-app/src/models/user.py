"""User ORM model and its dependencies."""

from models.base_class import Base
from models.soft_delete_mixin import SoftDeleteMixin
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column


class User(Base, SoftDeleteMixin):
    """User model to create and manipulate user entity in the database."""

    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    second_name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(50), nullable=False)

    @property
    def full_name(self) -> str:
        """Return the user's full name composed of first and second names."""
        return f"{self.first_name} {self.second_name}"
