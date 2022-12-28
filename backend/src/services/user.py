from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from src import models


def get_user_by_id(user_id: int, db: Session) -> models.User:
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="not found")
    return user
