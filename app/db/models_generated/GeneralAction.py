from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app.storingway.models_generated.Action import Action


class GeneralAction(SQLModel, table=True):
    __tablename__ = "general_action"
    __table_args__ = {'extend_existing': True}
    __allow_unmapped__ = True
    id: int = Field(default=None, primary_key=True)
    name: str
    description: str
    action_id: Optional[int] = Field(default=None, foreign_key="action.id")
    action: Optional["Action"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[GeneralAction.action_id]"})
    unlock_link: int
    recast: int
    u_i_priority: int
    icon: str

