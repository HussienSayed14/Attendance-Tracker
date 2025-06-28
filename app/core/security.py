import os, datetime
from jose import jwt, JWTError
from passlib.context import CryptContext
from fastapi import HTTPException, status

# ------------------------------------------------------------------
# Password hashing
# ------------------------------------------------------------------
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)

# ------------------------------------------------------------------
# JWT settings
# ------------------------------------------------------------------
SECRET_KEY = os.getenv("JWT_SECRET", "super-secret")  
ALGORITHM  = "HS256"
ACCESS_EXPIRE_DAYS = 7

def create_access_token(sub: str) -> str:
    """
    sub = subject (user id or email)
    """
    expire = datetime.datetime.utcnow() + datetime.timedelta(days=ACCESS_EXPIRE_DAYS)
    to_encode = {"exp": expire, "sub": sub}
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def decode_access_token(token: str) -> str:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload["sub"]
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")