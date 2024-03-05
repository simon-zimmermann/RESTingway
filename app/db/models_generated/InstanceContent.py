from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from db.models_generated.InstanceContentType import InstanceContentType
    from db.models_generated.BGM import BGM
    from db.models_generated.Cutscene import Cutscene
    from db.models_generated.Colosseum import Colosseum
    from db.models_generated.InstanceContentTextData import InstanceContentTextData
    from db.models_generated.BNpcBase import BNpcBase
    from db.models_generated.InstanceContentRewardItem import InstanceContentRewardItem
    from db.models_generated.InstanceContentBuff import InstanceContentBuff


class InstanceContent(SQLModel, table=True):
    __tablename__ = "instance_content"
    __table_args__ = {'extend_existing': True}
    __allow_unmapped__ = True
    id: int = Field(default=None, primary_key=True)
    instance_content_type_id: Optional[int] = Field(default=None, foreign_key="instance_content_type.id")
    instance_content_type: Optional["InstanceContentType"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[InstanceContent.instance_content_type_id]"})
    week_restriction: int
    time_limitmin: int
    b_g_m_id: Optional[int] = Field(default=None, foreign_key="b_g_m.id")
    b_g_m: Optional["BGM"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[InstanceContent.b_g_m_id]"})
    win_b_g_m_id: Optional[int] = Field(default=None, foreign_key="b_g_m.id")
    win_b_g_m: Optional["BGM"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[InstanceContent.win_b_g_m_id]"})
    cutscene_id: Optional[int] = Field(default=None, foreign_key="cutscene.id")
    cutscene: Optional["Cutscene"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[InstanceContent.cutscene_id]"})
    l_g_b_event_range: int
    order: int
    colosseum_id: Optional[int] = Field(default=None, foreign_key="colosseum.id")
    colosseum: Optional["Colosseum"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[InstanceContent.colosseum_id]"})
    instance_content_text_data_boss_start_id: Optional[int] = Field(default=None, foreign_key="instance_content_text_data.id")
    instance_content_text_data_boss_start: Optional["InstanceContentTextData"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[InstanceContent.instance_content_text_data_boss_start_id]"})
    instance_content_text_data_boss_end_id: Optional[int] = Field(default=None, foreign_key="instance_content_text_data.id")
    instance_content_text_data_boss_end: Optional["InstanceContentTextData"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[InstanceContent.instance_content_text_data_boss_end_id]"})
    b_npc_base_boss_id: Optional[int] = Field(default=None, foreign_key="b_npc_base.id")
    b_npc_base_boss: Optional["BNpcBase"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[InstanceContent.b_npc_base_boss_id]"})
    instance_content_text_data_objective_start_id: Optional[int] = Field(default=None, foreign_key="instance_content_text_data.id")
    instance_content_text_data_objective_start: Optional["InstanceContentTextData"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[InstanceContent.instance_content_text_data_objective_start_id]"})
    instance_content_text_data_objective_end_id: Optional[int] = Field(default=None, foreign_key="instance_content_text_data.id")
    instance_content_text_data_objective_end: Optional["InstanceContentTextData"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[InstanceContent.instance_content_text_data_objective_end_id]"})
    sort_key: int
    new_player_bonus_gil: int
    new_player_bonus_exp: int
    new_player_bonus_a: int
    new_player_bonus_b: int
    final_boss_exp: int
    final_boss_currency_a: int
    final_boss_currency_b: int
    final_boss_currency_c: int
    boss_exp0: int
    boss_exp1: int
    boss_exp2: int
    boss_exp3: int
    boss_exp4: int
    boss_currency_a0: int
    boss_currency_a1: int
    boss_currency_a2: int
    boss_currency_a3: int
    boss_currency_a4: int
    boss_currency_b0: int
    boss_currency_b1: int
    boss_currency_b2: int
    boss_currency_b3: int
    boss_currency_b4: int
    boss_currency_c0: int
    boss_currency_c1: int
    boss_currency_c2: int
    boss_currency_c3: int
    boss_currency_c4: int
    instance_clear_exp: int
    instance_clear_gil: int
    instance_content_reward_item_id: Optional[int] = Field(default=None, foreign_key="instance_content_reward_item.id")
    instance_content_reward_item: Optional["InstanceContentRewardItem"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[InstanceContent.instance_content_reward_item_id]"})
    instance_content_buff_id: Optional[int] = Field(default=None, foreign_key="instance_content_buff.id")
    instance_content_buff: Optional["InstanceContentBuff"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[InstanceContent.instance_content_buff_id]"})
    req_instance_id: Optional[int] = Field(default=None, foreign_key="instance_content.id")
    req_instance: Optional["InstanceContent"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[InstanceContent.req_instance_id]"})
    party_condition: int

