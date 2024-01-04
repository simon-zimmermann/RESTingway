from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app.storingway.models_generated.Status import Status


class ActionProcStatus(SQLModel, table=True):
    __tablename__ = "action_proc_status"
    __table_args__ = {'extend_existing': True}
    __allow_unmapped__ = True
    id: int = Field(default=None, primary_key=True)
    status_id: Optional[int] = Field(default=None, foreign_key="status.id")
    status: Optional["Status"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[ActionProcStatus.status_id]"})

