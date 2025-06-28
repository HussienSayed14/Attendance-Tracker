from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.api.deps import get_db, get_current_user, has_permission
from typing import List
from app.models.user import User
from app.schemas.user import UserOut, UserStatusUpdate
from app.services.admin_service import AdminService

router = APIRouter(prefix="/admin", tags=["admin"])

@router.get("/users", response_model=List[UserOut])
def get_users(
    status: str = Query(..., description="Filter users by status: 'active' or 'inactive' or 'all'"),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if not has_permission(current_user, "can_manage_access"):
        raise HTTPException(status_code=403, detail="Permission denied")
    
    if status not in ["active", "inactive", "all"]:
        raise HTTPException(status_code=400, detail="Invalid status filter. Use 'active', 'inactive', or 'all'.")
    return AdminService.get_users(db, status)


@router.patch("/users/update", response_model=UserOut)
def update_user_status(
    paylaod: UserStatusUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if not has_permission(current_user, "can_manage_access"):
        raise HTTPException(status_code=403, detail="Permission denied")
    
    if not paylaod.id or paylaod.is_active is None:
        raise HTTPException(status_code=400, detail="User ID is required and is_active must be provided.")
    
    return AdminService.update_user_status(db, paylaod.id, paylaod.is_active)