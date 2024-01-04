from typing import Optional
from sqlmodel import Field, SQLModel, Relationship


class ENpcResident(SQLModel, table=True):
    __tablename__ = "e_npc_resident"
    __table_args__ = {'extend_existing': True}
    __allow_unmapped__ = True
    id: int = Field(default=None, primary_key=True)
    singular: str
    adjective: int
    plural: str
    possessive_pronoun: int
    starts_with_vowel: int
    pronoun: int
    article: int
    title: str
    map: int

