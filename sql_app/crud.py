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
    db_book = models.Book(title=book.title, author=book.author, user_id=user.id)
    session.add(db_book)
    return db_book


def get_book_by_title(session: Session, title: str):
    return session.query(models.Book).filter(models.Book.title == title).all()


def get_books_by_user(session: Session):
    return session.query(models.User).get('books')


def delete_user(session: Session, user_id: int):
    db_user = session.query(models.User).get(user_id)
    session.delete(db_user)
    session.commit()
    return 'DELETE USER SUCCESSFULLY'
