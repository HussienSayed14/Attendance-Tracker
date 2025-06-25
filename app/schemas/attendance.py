# app/schemas/attendance.py
from pydantic import BaseModel
from datetime import date
from typing import List, Literal

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