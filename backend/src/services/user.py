from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from src import models, schemas, utils


def get_user_by_id(user_id: int, db: Session) -> models.User:
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="not found")
    return user


def create_new_user(user: schemas.UserCreate, db: Session) -> models.User:
    user.password = utils.hash(user.password)
    new_user = models.User(**user.dict())
    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="user already exists"
        )
    return new_user
