# models/logic_audit.py

from sqlalchemy import Boolean, Column, ForeignKey, String, Integer, DateTime, Text, func
from app.core.database import Base
from app.crud import user
from sqlalchemy.orm import relationship

# ────── Logic Audit Model ────────────────────────────────────────────────
class LogicAudit(Base):
    __tablename__ = "logic_audit"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer,ForeignKey("users.id") ,nullable=False)
    status = Column(Boolean, nullable=False)  # True for success, False for failure
    description = Column(Text, nullable=False)  # Description of the logic executed
    timestamp = Column(DateTime(timezone=True), server_default=func.now())


    # ────── Relationships ────────────────────────────────────────────────
    user = relationship("User", backref="logic_audits")
