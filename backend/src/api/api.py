from fastapi import APIRouter

from src.api.endpoints import users
from src.db.database import SessionLocal

router: APIRouter = APIRouter()

router.include_router(users.router)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
