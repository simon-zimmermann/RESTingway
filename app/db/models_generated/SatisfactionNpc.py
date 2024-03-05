from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from db.models_generated.ENpcResident import ENpcResident
    from db.models_generated.Quest import Quest
    from db.models_generated.Item import Item


class SatisfactionNpc(SQLModel, table=True):
    __tablename__ = "satisfaction_npc"
    __table_args__ = {'extend_existing': True}
    __allow_unmapped__ = True
    id: int = Field(default=None, primary_key=True)
    npc_id: Optional[int] = Field(default=None, foreign_key="e_npc_resident.id")
    npc: Optional["ENpcResident"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[SatisfactionNpc.npc_id]"})
    quest_required_id: Optional[int] = Field(default=None, foreign_key="quest.id")
    quest_required: Optional["Quest"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[SatisfactionNpc.quest_required_id]"})
    level_unlock: int
    deliveries_per_week: int
    supply_index0: int
    supply_index1: int
    supply_index2: int
    supply_index3: int
    supply_index4: int
    supply_index5: int
    satisfaction_required0: int
    satisfaction_required1: int
    satisfaction_required2: int
    satisfaction_required3: int
    satisfaction_required4: int
    satisfaction_required5: int
    item00_id: Optional[int] = Field(default=None, foreign_key="item.id")
    item00: Optional["Item"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[SatisfactionNpc.item00_id]"})
    item10_id: Optional[int] = Field(default=None, foreign_key="item.id")
    item10: Optional["Item"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[SatisfactionNpc.item10_id]"})
    item20_id: Optional[int] = Field(default=None, foreign_key="item.id")
    item20: Optional["Item"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[SatisfactionNpc.item20_id]"})
    item30_id: Optional[int] = Field(default=None, foreign_key="item.id")
    item30: Optional["Item"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[SatisfactionNpc.item30_id]"})
    item40_id: Optional[int] = Field(default=None, foreign_key="item.id")
    item40: Optional["Item"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[SatisfactionNpc.item40_id]"})
    item50_id: Optional[int] = Field(default=None, foreign_key="item.id")
    item50: Optional["Item"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[SatisfactionNpc.item50_id]"})
    item_count00: int
    item_count10: int
    item_count20: int
    item_count30: int
    item_count40: int
    item_count50: int
    is_h_q00: bool
    is_h_q10: bool
    is_h_q20: bool
    is_h_q30: bool
    is_h_q40: bool
    is_h_q50: bool
    item01_id: Optional[int] = Field(default=None, foreign_key="item.id")
    item01: Optional["Item"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[SatisfactionNpc.item01_id]"})
    item11_id: Optional[int] = Field(default=None, foreign_key="item.id")
    item11: Optional["Item"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[SatisfactionNpc.item11_id]"})
    item21_id: Optional[int] = Field(default=None, foreign_key="item.id")
    item21: Optional["Item"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[SatisfactionNpc.item21_id]"})
    item31_id: Optional[int] = Field(default=None, foreign_key="item.id")
    item31: Optional["Item"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[SatisfactionNpc.item31_id]"})
    item41_id: Optional[int] = Field(default=None, foreign_key="item.id")
    item41: Optional["Item"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[SatisfactionNpc.item41_id]"})
    item51_id: Optional[int] = Field(default=None, foreign_key="item.id")
    item51: Optional["Item"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[SatisfactionNpc.item51_id]"})
    item_count01: int
    item_count11: int
    item_count21: int
    item_count31: int
    item_count41: int
    item_count51: int
    is_h_q01: bool
    is_h_q11: bool
    is_h_q21: bool
    is_h_q31: bool
    is_h_q41: bool
    is_h_q51: bool
    item02_id: Optional[int] = Field(default=None, foreign_key="item.id")
    item02: Optional["Item"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[SatisfactionNpc.item02_id]"})
    item12_id: Optional[int] = Field(default=None, foreign_key="item.id")
    item12: Optional["Item"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[SatisfactionNpc.item12_id]"})
    item22_id: Optional[int] = Field(default=None, foreign_key="item.id")
    item22: Optional["Item"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[SatisfactionNpc.item22_id]"})
    item32_id: Optional[int] = Field(default=None, foreign_key="item.id")
    item32: Optional["Item"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[SatisfactionNpc.item32_id]"})
    item42_id: Optional[int] = Field(default=None, foreign_key="item.id")
    item42: Optional["Item"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[SatisfactionNpc.item42_id]"})
    item52_id: Optional[int] = Field(default=None, foreign_key="item.id")
    item52: Optional["Item"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[SatisfactionNpc.item52_id]"})
    item_count02: int
    item_count12: int
    item_count22: int
    item_count32: int
    item_count42: int
    item_count52: int
    is_h_q02: bool
    is_h_q12: bool
    is_h_q22: bool
    is_h_q32: bool
    is_h_q42: bool
    is_h_q52: bool
    icon: str

