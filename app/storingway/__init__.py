from sqlmodel import create_engine

from ..config import config


engine = create_engine(config.sqlite_url)
