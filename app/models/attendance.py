from sqlalchemy import (
    Column, Integer, Date, Enum, ForeignKey, Index
)
from sqlalchemy.orm import relationship
from app.core.database import Base
import enum


class AttendanceStatus(str, enum.Enum):
    onsite  = "on-site"
    remote  = "remote"
    leave   = "leave"
    night   = "night"
    absent  = "absent"


class Attendance(Base):
    __tablename__ = "attendance"

    id      = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    date    = Column(Date, nullable=False)                 # references WorkDay.date logically
    status  = Column(Enum(AttendanceStatus), nullable=False)

    # ────── relationships ────────────────────────────────────────────────
    user = relationship("User", backref="attendance")

    # ────── constraints / indexes ────────────────────────────────────────
    __table_args__ = (
        Index("idx_attendance_user_date", "user_id", "date", unique=True),
    )