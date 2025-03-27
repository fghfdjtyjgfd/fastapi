from typing import Optional
from pydantic import BaseModel
from datetime import datetime

# Step 3: Pydantic model ================================
# =================== Item schema =======================
# 3.1 - Base
class ItemBase(BaseModel):
    title: str
    price: float
    description: str

# 3.2 Request
class ItemCreate(ItemBase):
    pass

# 3.3 Response
class ItemResponse(ItemBase):
    id: int
    create_at: datetime
    update_at: datetime
    delete_at: Optional[datetime] = None
    class Config:
        from_attributes = True

# =================== User schema =======================

class UserBase(BaseModel):
    username: str
    password: str
    email: str

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    id: int
    create_at: datetime
    update_at: datetime
    delete_at: datetime

    class Config:
        from_attributes = True