from typing import Optional
from sqlmodel import Field, SQLModel, Relationship


class InstanceContentTextData(SQLModel, table=True):
    __tablename__ = "instance_content_text_data"
    __table_args__ = {'extend_existing': True}
    __allow_unmapped__ = True
    id: int = Field(default=None, primary_key=True)
    text: str

