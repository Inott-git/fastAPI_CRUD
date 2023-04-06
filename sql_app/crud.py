from sqlalchemy.orm import Session
from sql_app import models, schems


def create_user(session: Session, user: schems.UserCreate):
    db_user = models.User(login=user.login, password=user.password)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user


def create_book(session: Session, book: schems.BookCreate):
    db_book = models.Book(title=book.title, author=book.author, user_id=book.user_id)
    session.add(db_book)
    session.commit()
    session.refresh(db_book)
    return db_book


def get_user(session: Session, user_id: int):
    user = session.query(models.User).filter(models.User.user_id == user_id).first()
    if user == None:
        return {"user_id": -1,
                "login": '',
                "book": []
                }
    return user


def add_book(session: Session, user: schems.User, book: schems.Book):
    db_book = models.Book(title=book.title, author=book.author, user_id=user.user_id)
    session.add(db_book)
    return db_book


def delete_user(session: Session, user_id: int):
    db_user = session.query(models.User).get(user_id)
    if db_user == None:
        return {"user_id": -1,
                "login": '',
                "book": []
                }
    session.delete(db_user)
    session.commit()
    return 'DELETE USER SUCCESSFULLY'


def update_user(session: Session, user: schems.UserUpdate):
    db_user = session.query(models.User).get(user.user_id)
    if db_user == None:
        return {"user_id": -1,
                "login": '',
                "book": []
                }
    db_user.login = user.login
    db_user.password = user.password
    session.refresh(db_user)
    session.commit()
    return db_user
