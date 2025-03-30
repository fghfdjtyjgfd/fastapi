from sqlalchemy import Column, Integer, String, DateTime
from ..db.database import Base
from ..service.utils import get_thai_time

class TokenBlacklist(Base):
    __tablename__ = "token_blacklist"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    token = Column(String(length=500), nullable=False, unique=True, index=True)
    blacklisted_at = Column(DateTime(timezone=True), default=get_thai_time(), nullable=False)
    expire_at = Column(DateTime(timezone=True), nullable=False)