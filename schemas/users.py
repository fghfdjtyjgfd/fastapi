from pydantic import BaseModel, EmailStr, constr
from typing import List
from datetime import datetime
from .items import ItemResponse

class Usercreate(BaseModel):
    username: constr(min_length=3, max_length=15)
    password: constr(min_length=4)
    email: EmailStr

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    create_at: datetime
    update_at: datetime
    items: List[ItemResponse] = []

    class Config:
        from_attributes = True

# ======== User Login =========

class UserLogin(BaseModel):
    username: str
    password: str