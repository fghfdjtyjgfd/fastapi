from sqlalchemy import Column, DateTime, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from ..service.utils import get_thai_time
from ..db.database import Base

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

    owner_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    owner = relationship("Users", back_populates="items")

    def soft_delete(self):
        self.delete_at = get_thai_time()