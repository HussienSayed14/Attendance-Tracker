from datetime import date
from calendar import monthrange
from typing import Dict
from sqlalchemy import func, case
from sqlalchemy.orm import Session
from app.models.work_day import WorkDay
from app.models.attendance import Attendance
from app.schemas.attendance import AttendanceSummary

def get_summary(db: Session, user_id: int, year: int, month: int) -> AttendanceSummary:
    first_day = date(year, month, 1)
    last_day  = date(year, month, monthrange(year, month)[1])

    # --- working days vs holidays ---
    wd_totals = (
        db.query(
            func.count().label("total"),
            func.sum(case((WorkDay.is_holiday, 1), else_=0)).label("holidays")
        )
        .filter(WorkDay.date.between(first_day, last_day))
        .filter(func.extract("dow", WorkDay.date).notin_((5, 6)))      # Fri(5), Sat(6)
        .first()
    )
    total_wd  = wd_totals.total - wd_totals.holidays # type: ignore
    holidays  = wd_totals.holidays # type: ignore

    # --- attendance counts by status ---
    rows = (
        db.query(Attendance.status, func.count().label("cnt"))
        .filter(
            Attendance.user_id == user_id,
            Attendance.date.between(first_day, last_day)
        )
        .group_by(Attendance.status)
        .all()
    )
    counts: Dict[str, int] = {
        (r.status.value if hasattr(r.status, "value") else r.status): r.cnt for r in rows
    }

    office = counts.get("office", 0)
    remote = counts.get("home", 0)
    leave  = counts.get("leave", 0)
    night  = counts.get("night", 0)
    absent = counts.get("absent", 0)

    required_initial   = round(total_wd * 0.6)
    required_after_exemptions = max(required_initial - night - leave, 0)
    remaining = max(required_after_exemptions - office, 0)

    return AttendanceSummary(
        year=year,
        month=month,
        total_working_days=total_wd,
        holidays=holidays,
        required_on_site_before_exemptions=required_initial,
        required_on_site_after_exemptions=required_after_exemptions,
        office_days=office,
        remote_days=remote,
        leave_days=leave,
        night_days=night,
        absent_days=absent,
        remaining_on_site=remaining,
    )