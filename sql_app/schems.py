from typing import List

from fastapi import HTTPException
from pydantic import BaseModel, validator, validate_arguments, root_validator


class BookBase(BaseModel):
    title: str
    author: str
    user_id: int
    class Config:
        orm_mode=True

class BookCreate(BookBase):
    pass

class Book(BookBase):
    book_id: int

class UserBase(BaseModel):
    login: str

class User(UserBase):
    user_id: int
    books: list[Book] = []

    @root_validator
    def val(cls, value: dict):
        if value["user_id"] == -1:
            return {'status_code': 100, 'detail': 'User not found'}
        return value


    class Config:
        orm_mode = True

class UserCreate(UserBase):
    password: str



