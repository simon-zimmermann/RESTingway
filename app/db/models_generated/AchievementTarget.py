from typing import Optional
from sqlmodel import Field, SQLModel, Relationship


class AchievementTarget(SQLModel, table=True):
    __tablename__ = "achievement_target"
    __table_args__ = {'extend_existing': True}
    __allow_unmapped__ = True
    id: int = Field(default=None, primary_key=True)
    type: int
    value: int

