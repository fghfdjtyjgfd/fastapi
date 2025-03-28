from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from ....db.schema import UserResponse, Usercreate, UserLogin, TokenResponse
from ....db.database import get_db
from sqlalchemy.orm import Session
from ....service.user_service import (
    create_user,
    create_access_token,
    get_current_user,
    authenticate_user
)

routes = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

@routes.post("/register", response_model=UserResponse)
def register_user(user: Usercreate, db: Session = Depends(get_db)):
    return create_user(db, user)

@routes.post("/login", response_model=TokenResponse)
def login(login_data: UserLogin, db: Session = Depends(get_db)):
    user = authenticate_user(db, login_data)
    access_token = create_access_token(
        data={"sub": user.username}
    )
    return {"access_token": access_token, "token_type": "bearer"}

@routes.post("/logout")
def logout(token: str = Depends(oauth2_scheme)):
    return {"message": "Successfully logged out"}
