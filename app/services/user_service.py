from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.schemas.user import LoginResponse, UserCreate
from app.models.user import User
from app.crud import user as crud_user
from app.services.login_audit_service import AuditService
from app.core.security import hash_password, verify_password, create_access_token

class UserService:
    """
    Orchestrates business rules for users.
    Routers call these methods instead of CRUD directly.
    """

    @staticmethod
    def register(db: Session, payload: UserCreate) -> User:

        # 1. email uniqueness
        if crud_user.get_by_email(db, payload.email):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered",
            )
        new_user = payload.copy(update={"password": hash_password(payload.password)})
        return crud_user.create(db, new_user)
    

     # ───────── Login ─────────
    @staticmethod
    def authenticate(db: Session, email: str, password: str) -> LoginResponse:
        user = crud_user.get_by_email(db, email)
        if not user or not verify_password(password, user.password_hash): # type: ignore
            if user:
                # Log the failed login attempt
                AuditService.create_log(
                    db=db,
                    user_id=user.id,  # type: ignore
                    success=False,
                    desc="Failed login attempt due to incorrect password"
                )
            raise HTTPException(status_code=401, detail="Incorrect email or password")
        
        if not user.is_active: # type: ignore
            # Log the failed login attempt
            AuditService.create_log(
                db=db,
                user_id=user.id,  # type: ignore
                success=False,
                desc="Failed login attempt due to inactive account"
            )
            raise HTTPException(status_code=403, detail="You account is not activated yet, please contact the administrator")
        # 2. Generate JWT token
        access_token = create_access_token(sub=str(user.id))
        # 3. Return user data along with token
        if not access_token:
            raise HTTPException(status_code=500, detail="Something went wrong, please try again later")
        # 4. Return user data along with token
        reponse = LoginResponse(
            access_token=access_token,
            id=user.id, # type: ignore
            name=user.name, # type: ignore
            email=user.email, # type: ignore
            token_type="bearer"
        )
        # 5. Log the successful login attempt
        AuditService.create_log(
            db=db,
            user_id=user.id,  # type: ignore
            success=True,
            desc="User logged in successfully"
        )
        return reponse
    
        
