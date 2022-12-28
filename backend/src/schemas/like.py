from pydantic import BaseModel


class LikeBase(BaseModel):
    post_id: int

    class Config:
        orm_mode = True


class Like(LikeBase):
    class Config:
        orm_mode = True
