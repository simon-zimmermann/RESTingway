from typing import Optional
from sqlmodel import Field, SQLModel, Relationship


class EventIconType(SQLModel, table=True):
    __tablename__ = "event_icon_type"
    __table_args__ = {'extend_existing': True}
    __allow_unmapped__ = True
    id: int = Field(default=None, primary_key=True)
    npc_icon_available: str
    map_icon_available: str
    npc_icon_invalid: str
    map_icon_invalid: str
    icon_range: int

