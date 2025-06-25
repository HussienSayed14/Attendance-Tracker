from sqlalchemy import Column, Integer, Date, Boolean, Text, Index
from app.core.database import Base


class WorkDay(Base):
    __tablename__ = "work_days"

    id          = Column(Integer, primary_key=True)
    date        = Column(Date, nullable=False, unique=True)
    is_holiday  = Column(Boolean, nullable=False, default=False)
    description = Column(Text, nullable=True)

    __table_args__ = (
        Index("idx_workday_date", "date"),
    )