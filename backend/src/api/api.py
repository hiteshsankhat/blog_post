from fastapi import APIRouter
from src.api.endpoints import auth, like, posts, users

router: APIRouter = APIRouter()

router.include_router(auth.router)
router.include_router(users.router)
router.include_router(posts.router)
router.include_router(like.router)
