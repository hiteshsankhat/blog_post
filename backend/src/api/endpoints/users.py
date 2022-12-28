from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from src import oauth
from src.db.database import get_db
from src.schemas import UserCreate, UserOut
from src.services import user as user_service

router: APIRouter = APIRouter(prefix="/users", tags=["User"])


@router.post(
    "/create-user", status_code=status.HTTP_201_CREATED, response_model=UserOut
)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return user_service.create_new_user(user, db)


@router.get("/me", response_model=UserOut)
def get_current_user(
    user_id: int = Depends(oauth.get_current_user), db: Session = Depends(get_db)
):
    return user_service.get_user_by_id(user_id, db)


@router.get("/{id}", response_model=UserOut)
def get_user(id: int, db: Session = Depends(get_db)):
    return user_service.get_user_by_id(id, db)
