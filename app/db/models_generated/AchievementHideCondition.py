from typing import Optional
from sqlmodel import Field, SQLModel, Relationship


class AchievementHideCondition(SQLModel, table=True):
    __tablename__ = "achievement_hide_condition"
    __table_args__ = {'extend_existing': True}
    __allow_unmapped__ = True
    id: int = Field(default=None, primary_key=True)
    hide_achievement: bool
    hide_name: bool
    hide_conditions: bool

