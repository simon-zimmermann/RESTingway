from typing import Optional
from sqlmodel import Field, SQLModel, Relationship


class UIColor(SQLModel, table=True):
    __tablename__ = "u_i_color"
    __table_args__ = {'extend_existing': True}
    __allow_unmapped__ = True
    id: int = Field(default=None, primary_key=True)
    u_i_foreground: int
    u_i_glow: int

