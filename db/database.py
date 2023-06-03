from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
 
 #Database checklist:
 #1. Database definition : database.py
 #2. Model definition : models.py
 #3. Create database : main.py
 #4. Schema definition : schemas.py
 #5. ORM functionality : db_user.py
 #6. API functionality: user.py

SQLALCHEMY_DATABASE_URL = "sqlite:///./fastapi-practice.db"
 
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
 
Base = declarative_base()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()


