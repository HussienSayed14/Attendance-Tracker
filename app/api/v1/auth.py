from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.api.deps import get_current_user
from app.models.user import User
from app.schemas.user import LoginRequest, LoginResponse, UserCreate, UserOut, UserRead
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

@router.get("/me", response_model=UserOut)
def get_me(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
   return UserService.refresh_user_session(db, current_user)
    