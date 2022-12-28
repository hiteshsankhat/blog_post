# Import all the models, so that Base has them before being
# imported by Alembic
from src.db.database import Base
from src.models import Like, Post, User
