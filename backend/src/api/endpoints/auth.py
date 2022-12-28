from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from src import models, oauth, utils
from src.db.database import get_db

router = APIRouter(tags=["Authentication"])


@router.post("/login")
def login(
    user_cred: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    user = db.query(models.User).filter(models.User.email == user_cred.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="invalid credentials"
        )
    if not utils.verify(user_cred.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="invalid credentials"
        )
    access_token = oauth.create_access_token(data={"user_id": user.id})
    return {"access_token": access_token, "token_type": "bearer"}
