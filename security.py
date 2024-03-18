from datetime import datetime, timedelta
from jose import jwt
from typing import Optional
from passlib.context import CryptContext

SECRET_KEY = "ce9057abc106aea60649a7c4c00daec139379ad898f4665774a25965c85404e4"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 15

pwd_context = CryptContext(
    schemes=["bcrypt"], deprecated="auto"
)

def create_hash_password(plain_password : str) -> str:
    return pwd_context.hash(plain_password)

def create_access_token(data : dict, expies_delta : Optional[timedelta] = None):
    to_encode = data.copy()
    if expies_delta:
        expire = datetime.utcnow() + expies_delta
    else:
        expire = datetime.utcnow() + timedelta(15)

    to_encode.update({"exp":expire})
    encoded_jwt = jwt.encode(
        to_encode, SECRET_KEY, ALGORITHM
    )
    return encoded_jwt



    