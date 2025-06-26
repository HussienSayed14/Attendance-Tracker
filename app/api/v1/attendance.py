# app/api/routes/attendance.py
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.api.deps import get_db, get_current_user
from typing import List
from datetime import date
from app.schemas.attendance import AttendanceSummary, SubmitAttendanceRequest, WorkDayWithStatus
from app.services.attendance_service import AttendanceService

router = APIRouter(prefix="/attendance", tags=["attendance"])

@router.post("/submit")
def submit_attendance(
    payload: SubmitAttendanceRequest,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    AttendanceService.submit_entries(db, current_user, payload.entries)
    return {"message": "Attendance submitted successfully"}


@router.get("/summary/{year}/{month}", response_model=AttendanceSummary)
def summary(
    year: int,
    month: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return AttendanceService.get_summary(db, current_user.id, year, month)




@router.get(
    "/calendar",
    response_model=List[WorkDayWithStatus],
    summary="List work days (with holiday flag) and the user's current status"
)
def get_calendar(
    start: date = Query(..., description="Start date (YYYY-MM-DD)"),
    end:   date = Query(..., description="End date (YYYY-MM-DD)"),
    db:    Session = Depends(get_db),
    current_user   = Depends(get_current_user)
):
    """
    Returns every working day between `start` and `end`, tells whether it's an
    official holiday, and shows the user's previously saved attendance status
    (or null if none).
    """
    return AttendanceService.calendar_range(db, current_user.id, start, end)