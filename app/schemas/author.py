from typing import Optional
from pydantic import BaseModel, EmailStr


class AuthorBase(BaseModel):
    email_address: Optional[EmailStr] = None
    username: Optional[str] = None


class AuthorCreate(AuthorBase):
    email_address: EmailStr
    pen_name: str
    password: str


class AuthorCreateModerator(AuthorCreate):
    moderator: bool = True


class AuthorCreateAdmin(AuthorCreate):
    admin: bool = True
    moderator: bool = True


class AuthorUpdate(AuthorBase):
    ...


class AuthorInDBBase(AuthorBase):
    id: Optional[int] = None
    pen_name: Optional[str] = None

    class Config:
        orm_mode = True


class AuthorInDB(AuthorInDBBase):
    hashed_password: str


class Author(AuthorInDBBase):
    ...
