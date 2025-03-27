from sqlalchemy import Column, Integer, String, DateTime
import sqlalchemy.dialects.postgresql as pg
from .database import Base
from ..service.utils import get_thai_time

# Step 2: create ORM class ===============================
class Item(Base):
    __tablename__ = "items"

    create_at = Column(
        DateTime(timezone=True),
        default=get_thai_time(),
        nullable=False,
    )
    update_at = Column(
        DateTime(timezone=True),
        default=get_thai_time(),
        nullable=True,
        onupdate=get_thai_time()
    )
    delete_at = Column(
        DateTime(timezone=True),
        nullable=True
    )
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    title = Column(String(length=255), index=True)
    description = Column(String(length=255), index=True)
    price = Column(Integer, index=True)

    def soft_delete(self):
        self.delete_at = get_thai_time()