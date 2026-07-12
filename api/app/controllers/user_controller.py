from sqlalchemy.orm import Session

from app.models.models import User
from app.schemas.user import UserCreate
from app.services import user_service


def get_all_users(db: Session) -> list[User]:
    return user_service.get_all_users(db)

def get_user_by_id(db: Session, user_id: int) -> User | None:
    return user_service.get_user_by_id(db, user_id)

def create_user(db: Session, user_in: UserCreate) -> User:
    return user_service.create_user(db, user_in)

def login_user(db: Session, username: str, password: str) -> User | None:
    return user_service.login_user(db, username, password)
