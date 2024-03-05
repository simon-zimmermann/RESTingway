from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from db.models_generated.JournalCategory import JournalCategory


class JournalGenre(SQLModel, table=True):
    __tablename__ = "journal_genre"
    __table_args__ = {'extend_existing': True}
    __allow_unmapped__ = True
    id: int = Field(default=None, primary_key=True)
    icon: str
    journal_category_id: Optional[int] = Field(default=None, foreign_key="journal_category.id")
    journal_category: Optional["JournalCategory"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[JournalGenre.journal_category_id]"})
    name: str

