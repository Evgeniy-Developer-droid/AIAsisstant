from datetime import datetime
from typing import Any, Optional
from pydantic import BaseModel, EmailStr, field_validator


class UserSettingsSchema(BaseModel):
    id: int


class UserSchema(BaseModel):
    id: int
    full_name: Optional[str] = None
    email: EmailStr
    is_active: bool
    created_at: datetime
    last_login: Optional[datetime] = None
    settings: UserSettingsSchema

