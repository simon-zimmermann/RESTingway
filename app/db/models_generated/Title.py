from typing import Optional
from sqlmodel import Field, SQLModel, Relationship


class Title(SQLModel, table=True):
    __tablename__ = "title"
    __table_args__ = {'extend_existing': True}
    __allow_unmapped__ = True
    id: int = Field(default=None, primary_key=True)
    masculine: str
    feminine: str
    is_prefix: bool
    order: int

