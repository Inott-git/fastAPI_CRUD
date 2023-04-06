from sqlalchemy.orm import Session
import docs
from sql_app.database import get_db
from sql_app import crud, schems
from fastapi import FastAPI, Depends

app = FastAPI(
    title='fastAPI_CRUD',
    version='0.0.1',
    contact={
        'name': 'Artem',
        'url': 'https://github.com/Inott-git'
    },
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
    """
    Добавляет книгу для пользователя
    + _title: str_
    + _author: str_
    + _user_id: int_

    Возвращает книгу
    """
    return crud.create_book(session=session, book=book)


@app.get("/get_user", response_model=schems.User, tags=['user'])
async def get_user(user_id: int, session: Session = Depends(get_db)):
    """
    Получает пользователя
    + _user_id: int_

    Возвращает пользователя
    """
    return crud.get_user(session=session, user_id=user_id)


@app.get('/get_book_for_user', tags=['user'], response_model=list[schems.Book])
async def get_book_for_user(user_id: int, session: Session = Depends(get_db)):
    """
    Получает книги пользователя
    + _user_id: int_

    Возвращает список книг
    """
    return crud.get_user(session=session, user_id=user_id).books


@app.delete('/delete_user', tags=['user'])
async def delete_user(user_id: int, session: Session = Depends(get_db)):
    """
    Удаляет пользвателя
    + _user_id: int_

    Возвращает успех или, если не найден пользователь, то ошибка
    """
    return crud.delete_user(session=session, user_id=user_id)


@app.put('/update_user', tags=['user'], response_model=schems.User)
async def update_user(user: schems.UserUpdate, session: Session = Depends(get_db)):
    """
    Обновляет пользвателя
    + _user_id: int_
    + _login: str_
    + _password: str_

    Возвращает пользователя без пароля в целях безопастности
    """
    return crud.update_user(session=session, user=user)
