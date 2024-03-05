from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from db.models_generated.Stain import Stain


class NpcEquip(SQLModel, table=True):
    __tablename__ = "npc_equip"
    __table_args__ = {'extend_existing': True}
    __allow_unmapped__ = True
    id: int = Field(default=None, primary_key=True)
    model_main_hand: str
    dye_main_hand_id: Optional[int] = Field(default=None, foreign_key="stain.id")
    dye_main_hand: Optional["Stain"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[NpcEquip.dye_main_hand_id]"})
    model_off_hand: str
    dye_off_hand_id: Optional[int] = Field(default=None, foreign_key="stain.id")
    dye_off_hand: Optional["Stain"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[NpcEquip.dye_off_hand_id]"})
    model_head: int
    dye_head_id: Optional[int] = Field(default=None, foreign_key="stain.id")
    dye_head: Optional["Stain"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[NpcEquip.dye_head_id]"})
    visor: bool
    model_body: int
    dye_body_id: Optional[int] = Field(default=None, foreign_key="stain.id")
    dye_body: Optional["Stain"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[NpcEquip.dye_body_id]"})
    model_hands: int
    dye_hands_id: Optional[int] = Field(default=None, foreign_key="stain.id")
    dye_hands: Optional["Stain"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[NpcEquip.dye_hands_id]"})
    model_legs: int
    dye_legs_id: Optional[int] = Field(default=None, foreign_key="stain.id")
    dye_legs: Optional["Stain"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[NpcEquip.dye_legs_id]"})
    model_feet: int
    dye_feet_id: Optional[int] = Field(default=None, foreign_key="stain.id")
    dye_feet: Optional["Stain"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[NpcEquip.dye_feet_id]"})
    model_ears: int
    dye_ears_id: Optional[int] = Field(default=None, foreign_key="stain.id")
    dye_ears: Optional["Stain"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[NpcEquip.dye_ears_id]"})
    model_neck: int
    dye_neck_id: Optional[int] = Field(default=None, foreign_key="stain.id")
    dye_neck: Optional["Stain"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[NpcEquip.dye_neck_id]"})
    model_wrists: int
    dye_wrists_id: Optional[int] = Field(default=None, foreign_key="stain.id")
    dye_wrists: Optional["Stain"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[NpcEquip.dye_wrists_id]"})
    model_left_ring: int
    dye_left_ring_id: Optional[int] = Field(default=None, foreign_key="stain.id")
    dye_left_ring: Optional["Stain"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[NpcEquip.dye_left_ring_id]"})
    model_right_ring: int
    dye_right_ring_id: Optional[int] = Field(default=None, foreign_key="stain.id")
    dye_right_ring: Optional["Stain"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[NpcEquip.dye_right_ring_id]"})

