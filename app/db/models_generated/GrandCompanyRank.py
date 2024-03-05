from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from db.models_generated.Quest import Quest


class GrandCompanyRank(SQLModel, table=True):
    __tablename__ = "grand_company_rank"
    __table_args__ = {'extend_existing': True}
    __allow_unmapped__ = True
    id: int = Field(default=None, primary_key=True)
    tier: int
    order: int
    max_seals: int
    required_seals: int
    icon_maelstrom: str
    icon_serpents: str
    icon_flames: str
    quest_maelstrom_id: Optional[int] = Field(default=None, foreign_key="quest.id")
    quest_maelstrom: Optional["Quest"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[GrandCompanyRank.quest_maelstrom_id]"})
    quest_serpents_id: Optional[int] = Field(default=None, foreign_key="quest.id")
    quest_serpents: Optional["Quest"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[GrandCompanyRank.quest_serpents_id]"})
    quest_flames_id: Optional[int] = Field(default=None, foreign_key="quest.id")
    quest_flames: Optional["Quest"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[GrandCompanyRank.quest_flames_id]"})

