from pydantic import BaseModel, EmailStr


class Users_Schema(BaseModel):

    id: int
    username: str
    email: EmailStr
    hash_password: str

    class Config:
        orm_mode = True

        