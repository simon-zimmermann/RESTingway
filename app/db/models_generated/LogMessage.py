from typing import Optional
from sqlmodel import Field, SQLModel, Relationship


class LogMessage(SQLModel, table=True):
    __tablename__ = "log_message"
    __table_args__ = {'extend_existing': True}
    __allow_unmapped__ = True
    id: int = Field(default=None, primary_key=True)
    log_kind: int
    text: str

