from typing import Optional
from sqlmodel import Field, SQLModel, Relationship


class ContentMemberType(SQLModel, table=True):
    __tablename__ = "content_member_type"
    __table_args__ = {'extend_existing': True}
    __allow_unmapped__ = True
    id: int = Field(default=None, primary_key=True)
    tanks_per_party: int
    healers_per_party: int
    melees_per_party: int
    ranged_per_party: int

