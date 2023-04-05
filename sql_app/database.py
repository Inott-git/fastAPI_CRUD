from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQL_DATABASE = create_engine("sqlite:///sql_app/database.db")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=SQL_DATABASE)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
