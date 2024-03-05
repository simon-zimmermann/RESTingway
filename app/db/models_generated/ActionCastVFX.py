from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from db.models_generated.VFX import VFX


class ActionCastVFX(SQLModel, table=True):
    __tablename__ = "action_cast_v_f_x"
    __table_args__ = {'extend_existing': True}
    __allow_unmapped__ = True
    id: int = Field(default=None, primary_key=True)
    v_f_x_id: Optional[int] = Field(default=None, foreign_key="v_f_x.id")
    v_f_x: Optional["VFX"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[ActionCastVFX.v_f_x_id]"})
