from pydantic_settings import BaseSettings
import os


class Config(BaseSettings):
    path_gamedata_csv: str = os.path.join("gamedata", "ffxiv-datamining", "csv")
    debug_limit_db_columns: int = 0
    debug_limit_db_rows: int = 0
    sqlite_url: str = "sqlite:///resources/RESTingway.db"
    filepath_parsingway_json: str = "resources/parsingway.json"


config = Config()
