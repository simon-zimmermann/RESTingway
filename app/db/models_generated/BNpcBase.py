from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from db.models_generated.Behavior import Behavior
    from db.models_generated.Battalion import Battalion
    from db.models_generated.LinkRace import LinkRace
    from db.models_generated.ModelChara import ModelChara
    from db.models_generated.BNpcCustomize import BNpcCustomize
    from db.models_generated.NpcEquip import NpcEquip
    from db.models_generated.ArrayEventHandler import ArrayEventHandler
    from db.models_generated.BNpcParts import BNpcParts


class BNpcBase(SQLModel, table=True):
    __tablename__ = "b_npc_base"
    __table_args__ = {'extend_existing': True}
    __allow_unmapped__ = True
    id: int = Field(default=None, primary_key=True)
    behavior_id: Optional[int] = Field(default=None, foreign_key="behavior.id")
    behavior: Optional["Behavior"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[BNpcBase.behavior_id]"})
    battalion_id: Optional[int] = Field(default=None, foreign_key="battalion.id")
    battalion: Optional["Battalion"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[BNpcBase.battalion_id]"})
    link_race_id: Optional[int] = Field(default=None, foreign_key="link_race.id")
    link_race: Optional["LinkRace"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[BNpcBase.link_race_id]"})
    rank: int
    scale: float
    model_chara_id: Optional[int] = Field(default=None, foreign_key="model_chara.id")
    model_chara: Optional["ModelChara"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[BNpcBase.model_chara_id]"})
    b_npc_customize_id: Optional[int] = Field(default=None, foreign_key="b_npc_customize.id")
    b_npc_customize: Optional["BNpcCustomize"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[BNpcBase.b_npc_customize_id]"})
    npc_equip_id: Optional[int] = Field(default=None, foreign_key="npc_equip.id")
    npc_equip: Optional["NpcEquip"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[BNpcBase.npc_equip_id]"})
    special: int
    s_e_pack: int
    array_event_handler_id: Optional[int] = Field(default=None, foreign_key="array_event_handler.id")
    array_event_handler: Optional["ArrayEventHandler"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[BNpcBase.array_event_handler_id]"})
    b_npc_parts_id: Optional[int] = Field(default=None, foreign_key="b_npc_parts.id")
    b_npc_parts: Optional["BNpcParts"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[BNpcBase.b_npc_parts_id]"})
    is_target_line: bool
    is_display_level: bool

