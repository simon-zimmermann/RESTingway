from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine
import os


SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
if os.path.exists('../sql_app.db'):
    os.remove('../sql_app.db')
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
TableBase = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
