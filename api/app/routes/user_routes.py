from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.controllers import user_controller
from app.core.database import get_db
from app.schemas.user import UserCreate, UserLogin, UserOut

from app.core.security import create_access_token, get_current_user
from app.models.models import User

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/", response_model=list[UserOut])
def get_all_users(db: Session = Depends(get_db)):
    return user_controller.get_all_users(db)


@router.get("/me", response_model=UserOut)
def get_me(current_user: User = Depends(get_current_user)):
    return current_user


@router.post("/create", response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return user_controller.create_user(db, user)


@router.post("/login")
def login(credentials: UserLogin, db: Session = Depends(get_db)):
    user = user_controller.login_user(db, credentials.username, credentials.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    token = create_access_token(user.id)
    return {"message": "Login successful", "user": user, "token": token}
