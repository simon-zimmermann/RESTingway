from typing import Optional
from sqlmodel import Field, SQLModel, Relationship


class ContentType(SQLModel, table=True):
    __tablename__ = "content_type"
    __table_args__ = {'extend_existing': True}
    __allow_unmapped__ = True
    id: int = Field(default=None, primary_key=True)
    name: str
    icon: str
    icon_duty_finder: str

