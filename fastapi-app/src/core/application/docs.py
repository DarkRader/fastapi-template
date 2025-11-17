"""Package for API Documentation."""

from typing import ClassVar, TypedDict


class TagMeta(TypedDict):
    """Metadata structure for describing OpenAPI documentation tags."""

    name: str
    description: str


class FastApiDocs:
    """Information for fastapi documentation."""

    NAME = "API template of the FastAPI projects"
    DESCRIPTION = (
        "This project serves as a FastAPI application template. "
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
    AUTHORISATION_TAG: ClassVar[TagMeta] = TagMeta(
        name="auth",
        description="Authorisation in OpenID.",
    )
    USER_TAG: ClassVar[TagMeta] = TagMeta(
        name="users",
        description="Operations with users.",
    )

    def get_tags_metadata(self) -> list[TagMeta]:
        """Get tags metadata."""
        return [
            self.AUTHORISATION_TAG,
            self.USER_TAG,
        ]


fastapi_docs = FastApiDocs()
