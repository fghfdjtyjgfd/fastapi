from datetime import datetime
from pydantic import BaseModel, conint
from typing import Optional

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