from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from db.models_generated.Quest import Quest


class MapCondition(SQLModel, table=True):
    __tablename__ = "map_condition"
    __table_args__ = {'extend_existing': True}
    __allow_unmapped__ = True
    id: int = Field(default=None, primary_key=True)
    quest_id: Optional[int] = Field(default=None, foreign_key="quest.id")
    quest: Optional["Quest"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[MapCondition.quest_id]"})

