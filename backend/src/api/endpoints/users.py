from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from src import models, oauth, utils
from src.db.database import get_db
from src.schemas import UserCreate, UserOut
from src.services import user as user_service

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


@router.get("/me", response_model=UserOut)
def get_current_user(
    user_id: int = Depends(oauth.get_current_user), db: Session = Depends(get_db)
):
    return user_service.get_user_by_id(user_id, db)


@router.get("/{id}", response_model=UserOut)
def get_user(id: int, db: Session = Depends(get_db)):
    return user_service.get_user_by_id(id, db)
