from fastapi import APIRouter

router: APIRouter = APIRouter(prefix="/users", tags=["User"])


@router.get("/login")
def login():
    return "success"
    