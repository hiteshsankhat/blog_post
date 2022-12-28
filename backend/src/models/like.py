from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from src.models.base_model import BaseModel


class Like(BaseModel):
    __tablename__ = "likes"

    user_id = Column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        primary_key=True,
    )
    post_id = Column(
        Integer,
        ForeignKey("posts.id", ondelete="CASCADE"),
        nullable=False,
        primary_key=True,
    )

    creator = relationship("User")
    post = relationship("Post")
