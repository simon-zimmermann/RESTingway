from sqlmodel import create_engine, SQLModel

from common import config

# The __init__.py files in those two modules will automatically import all python files in their directory
import db.models
import db.models_generated


engine = create_engine(config.db_url)

SQLModel.metadata.create_all(engine)
