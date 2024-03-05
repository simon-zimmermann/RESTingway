from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from db.models_generated.Action import Action


class MountAction(SQLModel, table=True):
    __tablename__ = "mount_action"
    __table_args__ = {'extend_existing': True}
    __allow_unmapped__ = True
    id: int = Field(default=None, primary_key=True)
    action0_id: Optional[int] = Field(default=None, foreign_key="action.id")
    action0: Optional["Action"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[MountAction.action0_id]"})
    action1_id: Optional[int] = Field(default=None, foreign_key="action.id")
    action1: Optional["Action"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[MountAction.action1_id]"})
    action2_id: Optional[int] = Field(default=None, foreign_key="action.id")
    action2: Optional["Action"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[MountAction.action2_id]"})
    action3_id: Optional[int] = Field(default=None, foreign_key="action.id")
    action3: Optional["Action"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[MountAction.action3_id]"})
    action4_id: Optional[int] = Field(default=None, foreign_key="action.id")
    action4: Optional["Action"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[MountAction.action4_id]"})
    action5_id: Optional[int] = Field(default=None, foreign_key="action.id")
    action5: Optional["Action"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[MountAction.action5_id]"})

