from pydantic_settings import BaseSettings
import os


class Config(BaseSettings):
    app_name: str = "Awesome API"
    admin_email: str = "a"
    items_per_user: int = 50
    path_gamedata_csv: str = os.path.join("gamedata", "ffxiv-datamining", "csv")
    delete_models_on_startup: bool = True


config = Config()
