from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    password: str

    class Config:
        orm_mode = True


class UserOut(BaseModel):
    id: int
    email: EmailStr

    class Config:
        orm_mode = True
