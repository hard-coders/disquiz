from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    username: str
    password: str


class User(UserBase):
    id: int
    username: str
    is_active: bool

    class Config:
        orm_mode = True


# --------------------------------------------------------------------------------------
# responses
# --------------------------------------------------------------------------------------
class ResponseId(BaseModel):
    id: int

    class Config:
        orm_mode = True
