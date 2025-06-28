from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.security import decode_access_token
from app.crud.user import get_by_id
from app.models.user import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(token: str = Depends(oauth2_scheme),
                     db: Session = Depends(get_db)):
    user_id = decode_access_token(token)
    user = get_by_id(db, int(user_id))
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
    return user



def has_permission(user: User, permission_name: str) -> bool:
    return any(p.permission.name == permission_name for p in user.permissions)