from typing import Optional
from sqlmodel import Field, SQLModel, Relationship


class InstanceContentBuff(SQLModel, table=True):
    __tablename__ = "instance_content_buff"
    __table_args__ = {'extend_existing': True}
    __allow_unmapped__ = True
    id: int = Field(default=None, primary_key=True)
    echo_start: int
    echo_death: int

