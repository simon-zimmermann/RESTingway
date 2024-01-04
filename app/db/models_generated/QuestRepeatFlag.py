from typing import Optional
from sqlmodel import Field, SQLModel, Relationship


class QuestRepeatFlag(SQLModel, table=True):
    __tablename__ = "quest_repeat_flag"
    __table_args__ = {'extend_existing': True}
    __allow_unmapped__ = True
    id: int = Field(default=None, primary_key=True)
    quest: int

