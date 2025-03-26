from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from .database import Base
from datetime import datetime
from zoneinfo import ZoneInfo
from ..service.utils import get_thai_time

# Step 2: create ORM class ===============================
class Item(Base):
    __tablename__ = "items"

    create_at = Column(
        DateTime(timezone=True),
        server_default=get_thai_time(),
        nullable=False
    )
    update_at = Column(
        DateTime(timezone=True),
        server_default=get_thai_time(),
        onupdate=get_thai_time(),
        nullable=True
    )
    delete_at = Column(
        DateTime(timezone=True),
        nullable=True
    )
    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    price = Column(Integer, index=True)