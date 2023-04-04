from typing import List

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sql_app.database import Base, SQL_DATABASE

class User(Base):
    __tablename__ = 'user'
    user_id = Column(Integer, autoincrement=True, primary_key=True)
    login = Column(String, nullable=False)
    password = Column(String, nullable=False)

    books = relationship("Book", back_populates='user')

class Book(Base):
    __tablename__ = 'book'
    book_id = Column(Integer, autoincrement=True, primary_key=True)
    title = Column(String)
    author = Column(String)
    user_id = Column(Integer, ForeignKey('user.user_id'))

    user = relationship("User", back_populates='books')

# Base.metadata.drop_all(SQL_DATABASE)
# Base.metadata.create_all(SQL_DATABASE)