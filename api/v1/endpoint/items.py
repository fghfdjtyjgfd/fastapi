from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from ....db.database import get_db
from ....db.schema import ItemCreate, ItemResponse
from ....db.models import Item
from .users import oauth2_scheme
from ....service.user_service import get_current_user

# Step 4: HTTP method CRUD ========================================

routes = APIRouter()

@routes.get("/", response_model=List[ItemResponse])
def get_items(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    current_user = get_current_user(db, token)
    db_items = db.query(Item).filter(
        Item.delete_at == None,
        Item.owner_id == current_user.id
    ).all()
    return db_items

@routes.get("/{item_id}", response_model=ItemResponse)
def get_item_by_id(item_id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    current_user = get_current_user(db, token)
    db_item = db.query(Item).filter(
        Item.id == item_id,
        Item.delete_at == None,
        Item.owner_id == current_user.id
    ).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@routes.post("/create", response_model=ItemResponse)
def create_items(item: ItemCreate, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    current_user = get_current_user(db, token)
    db_item = Item(
        title=item.title,
        description=item.description,
        price=item.price,
        owner_id=current_user.id
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@routes.put("/update/{item_id}", response_model=ItemResponse)
def edit_item(item_id: int, item: ItemCreate, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    current_user = get_current_user(db, token)
    db_item = db.query(Item).filter(
        Item.id == item_id,
        Item.delete_at == None,
        Item.owner_id == current_user.id
    ).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    for key, value in item.model_dump().items():
        setattr(db_item, key, value)
    db.commit()
    db.refresh(db_item)
    return db_item

@routes.delete("/delete/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    current_user = get_current_user(db, token)
    db_item = db.query(Item).filter(
        Item.id == item_id,
        Item.delete_at == None,
        Item.owner_id == current_user.id
    ).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db_item.soft_delete()
    db.commit()
    return {"message": "Item deleted"}