from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr
from src.schemas.user import UserOut


class PostBase(BaseModel):
    title: str
    content: str

    class Config:
        orm_mode = True


class PostCreate(PostBase):
    pass

    class Config:
        orm_mode = True


class PostOut(PostBase):
    creator: UserOut
    created_at: datetime
    pass

    class Config:
        orm_mode = True


class PostUpdate(BaseModel):
    title: Optional[str]
    content: Optional[str]
