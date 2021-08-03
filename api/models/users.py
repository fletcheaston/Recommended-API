from typing import Optional, Sequence

from django.db import models
from pydantic import EmailStr

from .base import BaseFilter, BaseList, BaseModel, BaseSaved, DatabaseModel


class DatabaseUser(DatabaseModel):
    name = models.TextField()
    email = models.TextField(
        unique=True,
    )
    hashed_password = models.TextField()
    image_url = models.TextField()


class UserSaved(BaseSaved):
    name: str
    email: EmailStr
    image_url: str


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str


class UserFilter(BaseFilter):
    search: Optional[str] = None


class UserList(BaseList):
    results: Sequence[UserSaved]


class UserLogin(BaseModel):
    email: EmailStr
    password: str
