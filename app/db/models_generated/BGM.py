from typing import Optional
from sqlmodel import Field, SQLModel, Relationship


class BGM(SQLModel, table=True):
    __tablename__ = "b_g_m"
    __table_args__ = {'extend_existing': True}
    __allow_unmapped__ = True
    id: int = Field(default=None, primary_key=True)
    file: str
    priority: int
    disable_restart_time_out: bool
    disable_restart: bool
    pass_end: bool
    disable_restart_reset_time: float
    special_mode: int

