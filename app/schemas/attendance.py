# app/schemas/attendance.py
from pydantic import BaseModel
from datetime import date
from typing import List, Literal, Optional

class AttendanceEntry(BaseModel):
    date: date
    status: Literal["onsite", "remote", "leave", "night"]

class SubmitAttendanceRequest(BaseModel):
    entries: List[AttendanceEntry]

    

# ----------  summary result ----------
class AttendanceSummary(BaseModel):
    year: int
    month: int
    total_working_days: int
    holidays: int
    required_on_site_before_exemptions: int
    required_on_site_after_exemptions: int
    office_days: int
    remote_days: int
    leave_days: int
    night_days: int
    absent_days: int
    remaining_on_site: int
    extra_days: int


class WorkDayWithStatus(BaseModel):
    date: date
    is_holiday: bool
    day_name: str          # e.g. "Monday"
    status: Optional[
        Literal["on-site", "remote", "leave", "night", "absent"]
    ] = None        # null if user never submitted

    class Config:
        orm_mode = True      # lets FastAPI read SQLAlchemy rows directly