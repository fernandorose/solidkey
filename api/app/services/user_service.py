from sqlalchemy.orm import Session

from app.core.security import hash_password
from app.models.models import User
from app.schemas.user import UserCreate


def get_all_users(db: Session) -> list[User]:
    return db.query(User).all()


def create_user(db: Session, user_in: UserCreate) -> User:
    user = User(
        username=user_in.username,
        email=user_in.email,
        password=hash_password(user_in.password),
        role=user_in.role,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
