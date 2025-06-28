from fastapi import FastAPI
from app.api.v1 import admin, auth
from app.api.v1 import attendance
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Attendance Tracker API")


# Allow requests from your frontend (adjust port if different)
origins = [
    "http://attendance-report-bucket.s3-website.eu-north-1.amazonaws.com",  # S3 bucket URL
    "http://localhost:5173",  # Vite default port
    "http://127.0.0.1:5173",  # Also valid
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["*"] to allow all
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(attendance.router)
app.include_router(admin.router)