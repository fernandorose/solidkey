from sqlalchemy.orm import Session

from app.models.models import User
from app.schemas.user import UserCreate
from app.services import user_service


def get_all_users(db: Session) -> list[User]:
    return user_service.get_all_users(db)


def create_user(db: Session, user_in: UserCreate) -> User:
    return user_service.create_user(db, user_in)
