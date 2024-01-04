from typing import Optional
from sqlmodel import Field, SQLModel, Relationship


class EmoteCategory(SQLModel, table=True):
    __tablename__ = "emote_category"
    __table_args__ = {'extend_existing': True}
    __allow_unmapped__ = True
    id: int = Field(default=None, primary_key=True)
    name: str

