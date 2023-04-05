from typing import Union, List

from sqlalchemy.orm import Session
import docs
from sql_app.database import SessionLocal, get_db
from sql_app import crud, schems, models
from fastapi import FastAPI, Request, Form, Depends, HTTPException

app = FastAPI(
    title='fastAPI_CRUD',
    version='0.0.1',
    openapi_tags=docs.tags_metadata
)


@app.post('/add_user', response_model=schems.User, tags=['user'], openapi_extra={'summary':'Добавление пользователя'})
async def add_user(user: schems.UserCreate, session: Session = Depends(get_db)):
    """
    Добавляет пользвателя
    + _login: str_
    + _password: str_

    Возвращает пользователя без пароля в целях безопастности
    """
    return crud.create_user(session=session, user=user)


@app.post('/add_book', response_model=schems.Book, tags=['book'])
async def add_book(book: schems.BookCreate, session: Session = Depends(get_db)):
    return crud.create_book(session=session, book=book)


@app.get("/get_user", response_model=schems.User, tags=['user'])
async def get_user(user_id: int, session: Session = Depends(get_db)):
    return crud.get_user(session=session, user_id=user_id)


@app.get('/get_book_for_user', tags=['user'], response_model=list[schems.Book])
async def get_book_for_user(user_id: int, session: Session = Depends(get_db)):
    return crud.get_user(session=session, user_id=user_id).books


@app.get('/get_book_by_title', response_model=list[schems.Book], tags=['book'])
async def get_book_by_title(title: str, session: Session = Depends(get_db)):
    return crud.get_book_by_title(session=session, title=title)


@app.delete('/delete_user', tags=['user'])
async def delete_user(user_id: int, session: Session = Depends(get_db)):
    return crud.delete_user(session=session, user_id=user_id)