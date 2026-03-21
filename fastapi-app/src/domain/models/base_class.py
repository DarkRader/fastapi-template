"""Module with SQLAlchemy base class used to create other models from this Base class."""

import uuid
from datetime import datetime
from uuid import uuid7

from core import get_utc_now, settings
from domain.models.soft_delete_mixin import SoftDeleteMixin
from sqlalchemy import UUID, DateTime, MetaData, func
from sqlalchemy.orm import DeclarativeBase, Mapped, declared_attr, mapped_column


class Base(DeclarativeBase, SoftDeleteMixin):
    """Base class of all ORM mapped models."""

    __abstract__ = True

    metadata = MetaData(naming_convention=settings.DB.NAMING_CONVENTION)

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid7,
        server_default=func.gen_random_uuid(),
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=get_utc_now,
        server_default=func.now(),
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
        onupdate=get_utc_now,
        server_onupdate=func.now(),
    )

    @declared_attr  # type: ignore[arg-type]
    def __tablename__(cls) -> str:  # noqa: N805  # declared_attr uses class method style
        """Generate a table name based on the lowercase class name."""
        return f"{cls.__name__.lower()}s"
