# app/api/routes/attendance.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.deps import get_db, get_current_user
from app.schemas.attendance import AttendanceSummary, SubmitAttendanceRequest
from app.services.attendance_service import AttendanceService

router = APIRouter(prefix="/attendance", tags=["attendance"])

@router.post("/submit")
def submit_attendance(
    payload: SubmitAttendanceRequest,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    AttendanceService.submit_entries(db, current_user.id, payload.entries)
    return {"message": "Attendance submitted successfully"}


@router.get("/summary/{year}/{month}", response_model=AttendanceSummary)
def summary(
    year: int,
    month: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return AttendanceService.get_summary(db, current_user.id, year, month)