from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app.storingway.models_generated.VFX import VFX


class StatusLoopVFX(SQLModel, table=True):
    __tablename__ = "status_loop_v_f_x"
    __table_args__ = {'extend_existing': True}
    __allow_unmapped__ = True
    id: int = Field(default=None, primary_key=True)
    v_f_x_id: Optional[int] = Field(default=None, foreign_key="v_f_x.id")
    v_f_x: Optional["VFX"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[StatusLoopVFX.v_f_x_id]"})
    v_f_x2_id: Optional[int] = Field(default=None, foreign_key="v_f_x.id")
    v_f_x2: Optional["VFX"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[StatusLoopVFX.v_f_x2_id]"})
    v_f_x3_id: Optional[int] = Field(default=None, foreign_key="v_f_x.id")
    v_f_x3: Optional["VFX"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[StatusLoopVFX.v_f_x3_id]"})

