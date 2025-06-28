from sqlalchemy import  Column,  String, Integer
from app.core.database import Base
from sqlalchemy.orm import relationship


class Permission(Base):
    __tablename__ = "permissions"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String)