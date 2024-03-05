from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from db.models_generated.UIColor import UIColor


class BeastReputationRank(SQLModel, table=True):
    __tablename__ = "beast_reputation_rank"
    __table_args__ = {'extend_existing': True}
    __allow_unmapped__ = True
    id: int = Field(default=None, primary_key=True)
    required_reputation: int
    name: str
    allied_names: str
    color_id: Optional[int] = Field(default=None, foreign_key="u_i_color.id")
    color: Optional["UIColor"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[BeastReputationRank.color_id]"})

