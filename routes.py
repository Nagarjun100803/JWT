from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import  OAuth2PasswordRequestForm
from datetime import timedelta

from sqlalchemy.orm import Session
import model, schema, auth, security  
from db import get_db

router = APIRouter()

@router.post("/register/", response_model=schema.UserInDBBase)
async def register(user_in : schema.UserIn, db : Session = Depends(get_db)):
    db_user = auth.get_user(db, username=user_in.username)
    if db_user:
        raise HTTPException(status_code=400,detail= "Username already exist")
    db_user = db.query(model.User).filter(model.User.email == user_in.email).first()
    if db_user:
                raise HTTPException(status_code=400,detail= "email already exist")
    hashed_password = security.create_hash_password(plain_password=user_in.password)
    db_user = model.User(**user_in.dict(exclude={"password"}), hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user 

@router.post("/token", response_model=schema.Token)
async def login_for_access_token(
       form_data : OAuth2PasswordRequestForm = Depends(), db : Session = Depends(get_db)):
        user = auth.get_user(db=db, username=form_data.username)
        if not user or not security.pwd_context.verify(form_data.password, user.hashed_password):
              raise HTTPException(status_code=401,
                                  detail="Incorrect username or password",
                                  headers={"WWW-Authenticate":"Bearer"})
        access_token_expires = timedelta(minutes=security.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = security.create_access_token(
               data = {"sub": user.username}, expies_delta=access_token_expires
        )
        return {"access_token" : access_token, "token_type" : "bearer"}

@router.get("/conversation/")
async def read_conversation(
       current_user : schema.UserInDB = Depends(auth.get_current_user)
):
    return {
          "converation" : "This is a conversation",
          "current_user" : current_user.username
    }
       

              


