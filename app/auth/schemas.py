from typing import Any, Optional
from pydantic import BaseModel, EmailStr, field_validator


class AuthInSchema(BaseModel):
    username: Optional[EmailStr] = None
    email: Optional[EmailStr] = None
    password: str


class AuthOutSchema(BaseModel):
    token: str


class RegisterUserInSchema(BaseModel):
    email: EmailStr
    name: Optional[str]
    password: str

    @field_validator("password")
    @classmethod
    def password_validate(cls, v):
        if not v:
            raise ValueError("Empty password")
        return v

