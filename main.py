from typing import Union

from sqlalchemy.orm import Session

from sql_app.database import SessionLocal, get_db
from sql_app import crud, schems, models
from fastapi import FastAPI, Request, Form, Depends


app = FastAPI()


@app.post('/add_user', response_model=schems.User)
async def add_user(user: schems.UserCreate, session: Session = Depends(get_db)):
    return crud.create_user(session=session, user=user)


@app.post('/add_book', response_model=schems.Book)
async def add_book(book: schems.BookCreate, session: Session = Depends(get_db)):
    return crud.create_book(session=session, book=book)

