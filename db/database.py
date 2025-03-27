from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from ..core.config import DATABASE_URL
from dotenv import load_dotenv
import os

load_dotenv()

host = os.getenv('MYSQL_HOST')
username = os.getenv('MYSQL_USERNAME')
password = os.getenv('MYSQL_PASSWORD')
database = os.getenv('MYSQL_DATABASE')

DATABASE_URL = f"mysql+pymysql://{username}:{password}@{host}/{database}"

# Step 1: create engine =============================

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
