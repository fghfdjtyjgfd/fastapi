from pydantic import BaseModel
from datetime import datetime

# Step 3: Pydantic model ================================

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
    class Config:
        from_attributes = True