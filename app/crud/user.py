from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate



def get_by_email(db: Session, email: str) -> User | None:
    return db.query(User).filter(User.email == email).first()

def get_by_id(db: Session, id: int) -> User | None:
    return db.query(User).filter(User.id == id).first()

def create(db: Session, user_in: UserCreate) -> User:
    db_user = User(
        name=user_in.name,
        email=user_in.email,
        password_hash=user_in.password,   # already hashed by service layer
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user