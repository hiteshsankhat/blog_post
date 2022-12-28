# Import all the models, so that Base has them before being
# imported by Alembic
from src.models.user import User  # noqa

from .database import Base  # noqa
