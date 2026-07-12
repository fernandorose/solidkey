import uuid
from datetime import datetime
from typing import List, Optional

from sqlalchemy import ForeignKey, String, Text, UniqueConstraint, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, server_default=func.gen_random_uuid()
    )
    username: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    role: Mapped[str] = mapped_column(String(50), nullable=False, server_default="user")
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    last_login: Mapped[Optional[datetime]] = mapped_column(nullable=True)

    passwords: Mapped[List["Password"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )
    categories: Mapped[List["PasswordCategory"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )


class Password(Base):
    __tablename__ = "passwords"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, server_default=func.gen_random_uuid()
    )
    user_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True
    )
    site_name: Mapped[str] = mapped_column(String(100), nullable=False)
    site_url: Mapped[str] = mapped_column(String(255), nullable=False)
    site_username: Mapped[str] = mapped_column(String(100), nullable=False)
    site_password: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        server_default=func.now(), onupdate=func.now()
    )

    user: Mapped["User"] = relationship(back_populates="passwords")
    categories: Mapped[List["PasswordCategory"]] = relationship(
        secondary="password_category_mapping", back_populates="passwords"
    )


class PasswordCategory(Base):
    __tablename__ = "password_categories"
    __table_args__ = (UniqueConstraint("user_id", "category_name"),)

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, server_default=func.gen_random_uuid()
    )
    user_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True
    )
    category_name: Mapped[str] = mapped_column(String(100), nullable=False)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        server_default=func.now(), onupdate=func.now()
    )

    user: Mapped["User"] = relationship(back_populates="categories")
    passwords: Mapped[List["Password"]] = relationship(
        secondary="password_category_mapping", back_populates="categories"
    )


class PasswordCategoryMapping(Base):
    __tablename__ = "password_category_mapping"

    password_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("passwords.id", ondelete="CASCADE"), primary_key=True
    )
    category_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("password_categories.id", ondelete="CASCADE"),
        primary_key=True,
        index=True,
    )
