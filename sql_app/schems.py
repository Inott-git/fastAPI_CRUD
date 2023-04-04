from typing import List

from pydantic import BaseModel

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


    class Config:
        orm_mode = True

class UserCreate(UserBase):
    password: str



