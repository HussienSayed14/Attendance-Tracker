
from sqlalchemy import  Column, Integer, ForeignKey
from app.core.database import Base
from sqlalchemy.orm import relationship

class UserPermission(Base):
    __tablename__ = "user_permissions"

    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    permission_id = Column(Integer, ForeignKey("permissions.id"), primary_key=True)

    # optional relationships
    user = relationship("User", back_populates="permissions")
    permission = relationship("Permission")