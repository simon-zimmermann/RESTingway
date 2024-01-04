from typing import Optional
from sqlmodel import Field, SQLModel, Relationship


class WeaponTimeline(SQLModel, table=True):
    __tablename__ = "weapon_timeline"
    __table_args__ = {'extend_existing': True}
    __allow_unmapped__ = True
    id: int = Field(default=None, primary_key=True)
    file: str
    next_weapon_timeline: int

