from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app.storingway.models_generated.JournalSection import JournalSection


class JournalCategory(SQLModel, table=True):
    __tablename__ = "journal_category"
    __table_args__ = {'extend_existing': True}
    __allow_unmapped__ = True
    id: int = Field(default=None, primary_key=True)
    name: str
    separate_type: int
    data_type: int
    journal_section_id: Optional[int] = Field(default=None, foreign_key="journal_section.id")
    journal_section: Optional["JournalSection"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[JournalCategory.journal_section_id]"})

