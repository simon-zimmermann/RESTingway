from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from db.models_generated.Balloon import Balloon


class Behavior(SQLModel, table=True):
    __tablename__ = "behavior"
    __table_args__ = {'extend_existing': True}
    __allow_unmapped__ = True
    id: int = Field(default=None, primary_key=True)
    condition0_target: int
    condition0_type: int
    balloon_id: Optional[int] = Field(default=None, foreign_key="balloon.id")
    balloon: Optional["Balloon"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Behavior.balloon_id]"})
    condition1_target: int
    condition1_type: int
    content_argument0: int
    content_argument1: int

