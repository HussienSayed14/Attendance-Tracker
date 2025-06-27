# app/schemas/logic_audit.py
from pydantic import BaseModel, Field

class AuditCreate(BaseModel):
    user_id: int
    status: bool
    description: str = Field(min_length=1, max_length=500)