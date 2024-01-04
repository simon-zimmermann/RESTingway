from typing import Optional
from sqlmodel import Field, SQLModel, Relationship


class Omen(SQLModel, table=True):
    __tablename__ = "omen"
    __table_args__ = {'extend_existing': True}
    __allow_unmapped__ = True
    id: int = Field(default=None, primary_key=True)
    path: str
    path_ally: str
    type: int
    restrict_y_scale: bool
    large_scale: bool

