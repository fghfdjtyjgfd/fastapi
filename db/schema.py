from typing import Optional, List
from pydantic import BaseModel, EmailStr, constr, conint
from datetime import datetime

# Step 3: Pydantic model ================================
# =================== Item schema =======================
# 3.1 - Base
class ItemBase(BaseModel):
    title: str
    price: conint(gt=0)
    description: Optional[str]

# 3.2 Request
class ItemCreate(ItemBase):
    pass

# 3.3 Response
class ItemResponse(ItemBase):
    id: int
    create_at: datetime
    update_at: datetime
    delete_at: Optional[datetime] = None
    owner_id: int
    class Config:
        from_attributes = True

# =================== User schema =======================
# ======== User create =========
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

class TokenResponse(BaseModel):
    access_token: str
    token_type: str