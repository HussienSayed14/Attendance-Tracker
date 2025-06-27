# app/crud/logic_audit.py
from sqlalchemy.orm import Session
from app.models.login_audit import LogicAudit
from app.schemas.login_audit import AuditCreate

def create(db: Session, payload: AuditCreate) -> LogicAudit:
    log = LogicAudit(
        user_id     = payload.user_id,
        status      = payload.status,
        description = payload.description,
    )
    db.add(log)
    db.commit()
    db.refresh(log)
    return log