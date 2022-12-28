from sqlalchemy import TIMESTAMP, Column, func
from src.db.database import Base


class BaseModel(Base):
    __abstract__ = True
    created_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=func.now()
    )
    update_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=func.now()
    )
