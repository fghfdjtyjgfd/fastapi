import jwt
from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from ....schemas.token import TokenResponse
from ....schemas.users import UserResponse, Usercreate, UserLogin
from ....db.database import get_db
from ....models.token import TokenBlacklist
from sqlalchemy.orm import Session
from ....service.utils import get_thai_time
from ....service.user_service import (
    create_user,
    create_access_token,
    authenticate_user,
    SECRET_KEY,
    ALGORITHM
)

routes = APIRouter(prefix="/users")

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
def logout(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, SECRET_KEY, ALGORITHM)
        exp_timestamp = payload.get("exp", 0)
        exp_datetime = datetime.fromtimestamp(exp_timestamp)

        blacklisted_token = TokenBlacklist(
            token=token,
            blacklisted_at=get_thai_time(),
            expire_at=exp_datetime
        )
        db.add(blacklisted_token)
        db.commit()
        return {"message": "Successfully logged out"}
    
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Logout failed: {e}"
        )
