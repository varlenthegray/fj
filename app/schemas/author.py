from typing import Optional
from pydantic import BaseModel, EmailStr


class AuthorBase(BaseModel):
    email_address: Optional[EmailStr] = None
    username: Optional[str] = None


class AuthorCreate(AuthorBase):
    email_address: EmailStr
    password: str


class AuthorCreateModerator(AuthorBase):
    moderator: bool = True
    email_address: str
    password: str


class AuthorCreateAdmin(AuthorBase):
    admin: bool = True
    email_address: str
    password: str


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
