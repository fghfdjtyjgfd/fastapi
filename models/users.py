from sqlalchemy import Column, String, Integer, DateTime
from ..service.utils import get_thai_time
from ..db.database import Base
from sqlalchemy.orm import relationship
import bcrypt

class Users(Base):
    __tablename__ = "users"

    create_at = Column(
        DateTime(timezone=True),
        default=get_thai_time(),
        nullable=False
    )
    update_at = Column(
        DateTime(timezone=True),
        default=get_thai_time(),
        onupdate=get_thai_time(),
        nullable=True
    )
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    username = Column(String(length=30), nullable=False, unique=True)
    hashed_password = Column(String(length=255), nullable=False)
    email = Column(String(length=30), nullable=False, unique=True)

    items = relationship("Item", back_populates="owner", cascade="all, delete-orphan")

    @classmethod
    def hash_password(cls, password: str) -> str:
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
   
    def verify_password(self, password: str) -> bool:
        return bcrypt.checkpw(
            password.encode('utf-8'),
            self.hashed_password.encode('utf-8')
        )