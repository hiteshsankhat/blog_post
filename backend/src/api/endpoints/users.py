from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from src import models, oauth, utils
from src.db.database import get_db
from src.schemas.user import UserBase, UserCreate

router: APIRouter = APIRouter(prefix="/users", tags=["User"])


@router.post("/create-user", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    user.password = utils.hash(user.password)
    new_user = models.User(**user.dict())
    try:
        db.add(new_user)
        db.commit()
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="user already exists"
        )
    db.refresh(new_user)
    return new_user
