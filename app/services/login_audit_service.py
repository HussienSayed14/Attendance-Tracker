# app/services/audit_service.py
from sqlalchemy.orm import Session
from app.schemas.login_audit import AuditCreate
from app.crud import login_audit as crud_audit

class AuditService:
    @staticmethod
    def create_log(db: Session, user_id: int, success: bool, desc: str):
        payload = AuditCreate(user_id=user_id, status=success, description=desc)
        crud_audit.create(db, payload)