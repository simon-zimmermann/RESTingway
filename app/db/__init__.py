from sqlmodel import create_engine, SQLModel

from app.common import config

# The __init__.py files in those two modules will automatically import all python files in their directory
import app.db.models
import app.db.models_generated


engine = create_engine(config.db_url)
