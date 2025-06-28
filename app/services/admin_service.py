from typing import List
from app.models.user import User
from app.schemas.user import UserOut
from sqlalchemy.orm import Session
from fastapi import HTTPException


class AdminService:

    @staticmethod
    def get_users(db: Session, status: str) -> List[UserOut]:
        if status == "all":
            users = db.query(User).all()
        elif status == "active":
            users = db.query(User).filter(User.is_active == True).all()
        elif status == "inactive":
            users = db.query(User).filter(User.is_active == False).all()

        else:      
            raise HTTPException(status_code=400, detail="Invalid status filter. Use 'active', 'inactive', or 'all'.")      
                
        return [
        UserOut(
            id=user.id, # type: ignore
            name=user.name, # type: ignore
            email=user.email, # type: ignore
            is_active=user.is_active, # type: ignore
            created_at=user.created_at, # type: ignore
            permissions=[up.permission.name for up in user.permissions] 
    )
    for user in users
]

    @staticmethod
    def update_user_status(db: Session, user_id: int, is_active: bool) -> UserOut:
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(status_code=400, detail="User not found")

        user.is_active = is_active # type: ignore
        db.commit()
        db.refresh(user)
        
        return UserOut.from_orm(user)
            
