from pydantic import BaseModel


class CreateUser(BaseModel):
    email: str
    username: str
    password: str


# --------------------------------------------------------------------------------------
# responses
# --------------------------------------------------------------------------------------
class ResponseId(BaseModel):
    id: int

    class Config:
        orm_mode = True


class ResponseUser(BaseModel):
    email: str
    username: str
    hashed_password: str
    is_active: bool

    class Config:
        orm_mode = True
