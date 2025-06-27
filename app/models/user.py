from datetime import datetime
from sqlalchemy import Boolean, Column, Integer, String, DateTime, ForeignKey, Index
from sqlalchemy.orm import relationship
from app.core.database import Base


class User(Base):
    __tablename__ = "users"

    id         = Column(Integer, primary_key=True, index=True)
    name       = Column(String(50), nullable=False)
    email      = Column(String(120), nullable=False, unique=True, index=True)
    password_hash = Column(String, nullable=False)
    is_active = Column(Boolean, default=False, nullable=False)
    manager_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    

    # ────── relationships ────────────────────────────────────────────────
    manager = relationship("User", remote_side=[id], backref="team")  # manager.team → list[User]

    # ────── indexes ──────────────────────────────────────────────────────
    __table_args__ = (
        Index("idx_user_manager", "manager_id"),
    )