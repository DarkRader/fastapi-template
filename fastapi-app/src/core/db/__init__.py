"""Package for modules which establish connection to database."""

from core.db.session import db_session

__all__ = [
    "db_session",
]
