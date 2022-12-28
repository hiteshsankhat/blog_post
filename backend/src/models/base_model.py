from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, String, func
from sqlalchemy.sql.expression import text
from src.db.database import Base


class BaseModel(Base):
    __abstract__ = True
    created_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=func.now()
    )
    update_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=func.now()
    )
