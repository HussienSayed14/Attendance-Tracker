from fastapi import FastAPI
from app.api.v1 import auth
from app.api.v1 import attendance

app = FastAPI(title="Attendance Tracker API")

app.include_router(auth.router)
app.include_router(attendance.router)