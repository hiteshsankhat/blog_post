from typing import List, Optional, Tuple, Union

from fastapi import HTTPException, status
from sqlalchemy import func
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from src import models, schemas


def get_all_post(db: Session, limit: int, skip: Optional[int]):
    posts = (
        db.query(models.Post, func.count(models.Like.post_id).label("likes"))
        .join(models.Like, models.Post.id == models.Like.post_id, isouter=True)
        .group_by(models.Post.id)
        .limit(limit)
        .offset(skip)
        .all()
    )
    return posts


def get_by_id(post_id: int, db: Session) -> models.Post:
    post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="not found")
    return post


def create_new_post(post: schemas.PostCreate, db: Session, user_id: int) -> models.Post:
    new_post = models.Post(**post.dict(), created_by_id=user_id)
    try:
        db.add(new_post)
        db.commit()
        db.refresh(new_post)
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="Post already exists"
        )
    return new_post


def delete_post(post_id: int, user_id: int, db: Session) -> None:
    post_query = db.query(models.Post).filter(models.Post.id == post_id)
    post = post_query.first()
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Post not found"
        )
    if post.created_by_id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Operation"
        )
    post_query.delete(synchronize_session=False)
    db.commit()


def update_posts(
    post_id: int, post: schemas.PostUpdate, user_id: int, db: Session
) -> Union[models.Post, None]:
    post_query = db.query(models.Post).filter(models.Post.id == post_id)
    post_from_db = post_query.first()
    if not post_from_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Post not found"
        )
    if post_from_db.created_by_id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Operation"
        )
    for field in post.dict(exclude_unset=True):
        setattr(post_from_db, field, getattr(post, field))
    db.commit()
    return post_query.first()
