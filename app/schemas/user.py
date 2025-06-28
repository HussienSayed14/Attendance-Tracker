from datetime import datetime
from pydantic import BaseModel, EmailStr, Field

from app.models import permissions

# Incoming payload
class UserCreate(BaseModel):
    name: str = Field(min_length=2, max_length=90)
    email: EmailStr
    password: str = Field(min_length=6)

# Outgoing response (never includes password_hash)
class UserRead(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        orm_mode = True


class LoginRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=6)

class LoginResponse(BaseModel):
    access_token: str
    id: int
    name: str
    email: EmailStr
    token_type: str = "bearer"
    permissions: list[str]


class UserStatusUpdate(BaseModel):
    id: int
    is_active: bool

    class Config:
        orm_mode = True


class UserOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    is_active: bool
    created_at: datetime
    permissions: list[str]

    class Config:
        orm_mode = True
        from_attributes = True
