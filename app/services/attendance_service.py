# app/services/attendance_service.py
from sqlalchemy.orm import Session
from app.models.attendance import Attendance
from app.models.user import User
from app.schemas.attendance import AttendanceEntry, AttendanceSummary
from typing import List
from app.crud import attendance as crud_att


class AttendanceService:
    @staticmethod
    def submit_entries(db: Session, user: User, entries: List[AttendanceEntry]):
        for entry in entries:
            existing = db.query(Attendance).filter_by(user_id=user.id, date=entry.date).first()
            if existing:
                existing.status = entry.status # type: ignore
            else:
                new_attendance = Attendance(
                    user_id=user.id,
                    date=entry.date,
                    status=entry.status
                )
                db.add(new_attendance)
        db.commit()



    @staticmethod
    def get_summary(db: Session, user_id: int, year: int, month: int) -> AttendanceSummary:
        return crud_att.get_summary(db, user_id, year, month)
