from pydantic import BaseModel, EmailStr, Field

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


class UserOut(BaseModel):
    id: int
    name: str
    email: EmailStr
