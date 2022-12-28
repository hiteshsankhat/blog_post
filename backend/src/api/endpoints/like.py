from typing import List, Optional

from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session
from src import oauth, schemas
from src.db.database import get_db
from src.services import like as like_service

router = APIRouter(prefix="/posts/{id}", tags=["Blog Posts like"])


@router.post("/like", status_code=status.HTTP_204_NO_CONTENT)
async def create_post(
    like: schemas.Like,
    user_id: int = Depends(oauth.get_current_user),
    db: Session = Depends(get_db),
):
    like_service.like_post(like, db, user_id)
