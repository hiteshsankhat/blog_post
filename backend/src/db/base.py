# Import all the models, so that Base has them before being
# imported by Alembic
from src.db.database import Base  # noqa
from src.models import Post  # noqa
from src.models import User  # noqa
