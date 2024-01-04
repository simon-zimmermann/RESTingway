from pydantic_settings import BaseSettings
import os


class Config(BaseSettings):
    path_gamedata_csv: str = os.path.join("gamedata", "ffxiv-datamining", "csv")
    debug_limit_db_columns: int = 0
    debug_limit_db_rows: int = 0
    debug_limit_universalis_scraper: int = 0
    db_url: str = "sqlite:///resources/RESTingway.db"
    # db_url: str = "mariadb+mariadbconnector://root@localhost:3306/restingway"
    filepath_parsingway_json: str = "resources/parsingway.json"


config = Config()
