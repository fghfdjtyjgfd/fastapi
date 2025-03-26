from fastapi import FastAPI
from .db.database import Base, engine
from .api.v1.endpoint import items

# create database
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(items.routes, prefix="/api/v1/items")

