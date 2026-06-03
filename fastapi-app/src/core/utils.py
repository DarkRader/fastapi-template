"""Utils for core module."""

from datetime import UTC, datetime


def get_utc_now() -> datetime:
    """Get the current UTC time."""
    return datetime.now(UTC)
