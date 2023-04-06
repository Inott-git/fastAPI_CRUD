from pydantic import BaseModel, root_validator


class BookBase(BaseModel):
    title: str
    author: str
    user_id: int

    class Config:
        orm_mode = True


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


class UserUpdate(UserBase):
    user_id: int
    password: str


class UserCreate(UserBase):
    password: str



