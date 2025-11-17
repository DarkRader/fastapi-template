"""DTO schemes for Data from OpenID Provider."""

from pydantic import BaseModel, EmailStr


class UserInfo(BaseModel):
    """Represent a user in the OpenID Provider."""

    sub: str
    preferred_username: str
    name: str
    given_name: str
    family_name: str
    email: EmailStr
    email_verified: bool
