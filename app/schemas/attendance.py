# app/schemas/attendance.py
from pydantic import BaseModel
from datetime import date
from typing import List, Literal

class AttendanceEntry(BaseModel):
    date: date
    status: Literal["office", "home", "leave", "night"]

class SubmitAttendanceRequest(BaseModel):
    entries: List[AttendanceEntry]