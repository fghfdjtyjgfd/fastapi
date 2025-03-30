from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
import sqlalchemy.dialects.postgresql as pg
from .database import Base
from ..service.utils import get_thai_time
import bcrypt

# Step 2: create ORM class ===============================
# ================= Item ORM class =======================
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

# ================= Users ORM class =======================
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
    
# ================= Blacklist token ORM class =======================

class TokenBlacklist(Base):
    __tablename__ = "token_blacklist"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    token = Column(String(length=500), nullable=False, unique=True, index=True)
    blacklisted_at = Column(DateTime(timezone=True), default=get_thai_time(), nullable=False)
    expire_at = Column(DateTime(timezone=True), nullable=False)