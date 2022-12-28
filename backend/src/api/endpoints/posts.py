from typing import Dict, List, Optional, Union

from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session
from src import oauth, schemas
from src.db.database import get_db
from src.services import post as post_service

router = APIRouter(prefix="/posts", tags=["Blog Posts"])


@router.get(
    "/",
    response_model=List[Dict[str, Union[schemas.PostOut, int]]],
    status_code=status.HTTP_200_OK,
)
async def get_all_post(
    limit: int = 10, skip: Optional[int] = None, db: Session = Depends(get_db)
):
    return post_service.get_all_post(db, limit, skip)


@router.post("/", response_model=schemas.PostOut, status_code=status.HTTP_201_CREATED)
async def create_post(
    post: schemas.PostCreate,
    user_id: int = Depends(oauth.get_current_user),
    db: Session = Depends(get_db),
):
    return post_service.create_new_post(post, db, user_id)


@router.get("/{id}", response_model=schemas.PostOut, status_code=status.HTTP_200_OK)
async def get(id: int, db: Session = Depends(get_db)):
    return post_service.get_by_id(post_id=id, db=db)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(
    id: int,
    user_id: int = Depends(oauth.get_current_user),
    db: Session = Depends(get_db),
):
    post_service.delete_post(id, user_id, db)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}", response_model=schemas.PostOut, status_code=status.HTTP_200_OK)
async def update_post(
    id: int,
    post: schemas.PostUpdate,
    user_id: int = Depends(oauth.get_current_user),
    db: Session = Depends(get_db),
):
    post = post_service.update_posts(id, post, user_id, db)
    return post
