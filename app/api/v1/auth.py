from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.schemas.user import LoginRequest, LoginResponse, UserCreate, UserRead
from app.services.user_service import UserService
from app.core.database import get_db

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def register(user_in: UserCreate, db: Session = Depends(get_db)):
    return UserService.register(db, user_in)



# ---------- login ----------
@router.post("/login", response_model=LoginResponse)
def login(payload: LoginRequest, db: Session = Depends(get_db)):
    return UserService.authenticate(db, payload.email, payload.password)