"""Package for API Documentation."""

from typing import ClassVar, TypedDict

from core import settings


class TagMeta(TypedDict):
    """Metadata structure for describing OpenAPI documentation tags."""

    name: str
    description: str


class FastApiDocs:
    """Information for fastapi documentation."""

    NAME = f"{settings.APP.NAME} of the {settings.APP.ORGANISATION}"
    DESCRIPTION = (
        "This project serves as a FastAPI application template. \n"
        "## API Conventions\n"
        "- `POST`\n\n"
        "  - Creates a record in collection\n\n"
        "  - Calls an action\n"
        "- `PUT`\n\n"
        "  - Updates object\n"
        "- `DELETE`\n\n"
        "  - Delete object\n\n"
        "## Authentication\n"
        "The application uses OpenID for authentication.\n\n"
        "### Supported grant types:\n"
        "- authorization_code"
    )
    VERSION = "0.1.0"
    WELL_KNOWN_TAG: ClassVar[TagMeta] = TagMeta(
        name="Well Known",
        description="Application health and readiness endpoints.",
    )
    AUTHORISATION_TAG: ClassVar[TagMeta] = TagMeta(
        name="Auth",
        description="Authorisation in OpenID.",
    )
    USER_TAG: ClassVar[TagMeta] = TagMeta(
        name="Users",
        description="Operations with users.",
    )

    def get_tags_metadata(self) -> list[TagMeta]:
        """Get tags metadata."""
        return [
            self.WELL_KNOWN_TAG,
            self.AUTHORISATION_TAG,
            self.USER_TAG,
        ]


fastapi_docs = FastApiDocs()
