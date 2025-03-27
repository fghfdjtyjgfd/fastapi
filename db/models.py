from sqlalchemy import Column, Integer, String, DateTime
import sqlalchemy.dialects.postgresql as pg
from .database import Base
from ..service.utils import get_thai_time
import uuid

# Step 2: create ORM class ===============================
class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    title = Column(String(length=255), index=True)
    description = Column(String(length=255), index=True)
    price = Column(Integer, index=True)