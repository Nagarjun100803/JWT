from fastapi import Depends, HTTPException, status 
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from sqlalchemy.orm import Session
import model, schema, security
from db import get_db

oauth_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_user(db : Session, username : str):
    return db.query(model.User).filter(model.User.username == username).first()

async def get_current_user(token : str = Depends(oauth_scheme), db : Session = Depends(get_db)):
    credientaial_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate your credientials",
        headers={"WWW-Authenticate": "Bearer"}
    )
    
    try: 
        payload = jwt.decode(token, security.SECRET_KEY,
                             algorithms=[security.ALGORITHM])
        username : str = payload.get("sub")
        if username is None:
            raise credientaial_exception
        token_data = schema.TokenData(username=username)
    except JWTError:                                                                            
        raise credientaial_exception
    user = get_user(db, username=token_data.username)
    if user is None:
        raise credientaial_exception
    return user 


