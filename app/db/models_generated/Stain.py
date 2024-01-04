from typing import Optional
from sqlmodel import Field, SQLModel, Relationship


class Stain(SQLModel, table=True):
    __tablename__ = "stain"
    __table_args__ = {'extend_existing': True}
    __allow_unmapped__ = True
    id: int = Field(default=None, primary_key=True)
    color: str
    shade: int
    sub_order: int
    name: str

