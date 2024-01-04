from typing import Optional
from sqlmodel import Field, SQLModel, Relationship


class GatheringItemLevelConvertTable(SQLModel, table=True):
    __tablename__ = "gathering_item_level_convert_table"
    __table_args__ = {'extend_existing': True}
    __allow_unmapped__ = True
    id: int = Field(default=None, primary_key=True)
    gathering_item_level: int
    stars: int

