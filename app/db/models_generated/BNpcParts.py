from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from db.models_generated.BNpcBase import BNpcBase


class BNpcParts(SQLModel, table=True):
    __tablename__ = "b_npc_parts"
    __table_args__ = {'extend_existing': True}
    __allow_unmapped__ = True
    id: int = Field(default=None, primary_key=True)
    b_npc_base1_id: Optional[int] = Field(default=None, foreign_key="b_npc_base.id")
    b_npc_base1: Optional["BNpcBase"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[BNpcParts.b_npc_base1_id]"})
    part_slot1: int
    x1: float
    y1: float
    z1: float
    scale1: float
    b_npc_base2_id: Optional[int] = Field(default=None, foreign_key="b_npc_base.id")
    b_npc_base2: Optional["BNpcBase"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[BNpcParts.b_npc_base2_id]"})
    part_slot2: int
    x2: float
    y2: float
    z2: float
    scale2: float
    b_npc_base3_id: Optional[int] = Field(default=None, foreign_key="b_npc_base.id")
    b_npc_base3: Optional["BNpcBase"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[BNpcParts.b_npc_base3_id]"})
    part_slot3: int
    x3: float
    y3: float
    z3: float
    scale3: int
    b_npc_base4_id: Optional[int] = Field(default=None, foreign_key="b_npc_base.id")
    b_npc_base4: Optional["BNpcBase"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[BNpcParts.b_npc_base4_id]"})
    part_slot4: int
    x4: float
    y4: float
    z4: float
    scale4: float
    b_npc_base5_id: Optional[int] = Field(default=None, foreign_key="b_npc_base.id")
    b_npc_base5: Optional["BNpcBase"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[BNpcParts.b_npc_base5_id]"})
    part_slot5: int
    x5: float
    y5: float
    z5: float
    scale5: float

