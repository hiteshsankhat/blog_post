from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from src import models, schemas


def like_post(like: schemas.Like, db: Session, user_id: int) -> None:
    like_query = db.query(models.Like).filter(
        models.Like.post_id == like.post_id, models.Like.user_id == user_id
    )
    found_like = like_query.first()
    if found_like:
        like_query.delete(synchronize_session=False)
    else:
        new_vote = models.Like(post_id=like.post_id, user_id=user_id)
        db.add(new_vote)
    db.commit()
