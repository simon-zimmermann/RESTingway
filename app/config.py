from pydantic_settings import BaseSettings


class Config(BaseSettings):
    app_name: str = "Awesome API"
    admin_email: str = "a"
    items_per_user: int = 50
    path_gamedata_csv: str = "gamedata/ffxiv-datamining/csv"


config = Config()
