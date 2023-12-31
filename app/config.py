from pydantic_settings import BaseSettings
import os


class Config(BaseSettings):
    app_name: str = "Awesome API"
    admin_email: str = "a"
    items_per_user: int = 50
    path_gamedata_csv: str = os.path.join("gamedata", "ffxiv-datamining", "csv")
    delete_models_on_startup: bool = True
    debug_limit_db_columns: int = 0
    debug_limit_db_rows: int = 0
    sqlite_file_name: str = "sql_app.db"
    sqlite_url: str = f"sqlite:///{sqlite_file_name}"
    parsingway_json_filepath: str = "resources/parsingway.json"


config = Config()
