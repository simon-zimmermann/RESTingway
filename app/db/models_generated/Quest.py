from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from db.models_generated.ExVersion import ExVersion
    from db.models_generated.ClassJobCategory import ClassJobCategory
    from db.models_generated.ClassJob import ClassJob
    from db.models_generated.GrandCompany import GrandCompany
    from db.models_generated.GrandCompanyRank import GrandCompanyRank
    from db.models_generated.InstanceContent import InstanceContent
    from db.models_generated.Festival import Festival
    from db.models_generated.BeastTribe import BeastTribe
    from db.models_generated.BeastReputationRank import BeastReputationRank
    from db.models_generated.SatisfactionNpc import SatisfactionNpc
    from db.models_generated.Mount import Mount
    from db.models_generated.DeliveryQuest import DeliveryQuest
    from db.models_generated.Level import Level
    from db.models_generated.Behavior import Behavior
    from db.models_generated.QuestRepeatFlag import QuestRepeatFlag
    from db.models_generated.QuestClassJobSupply import QuestClassJobSupply
    from db.models_generated.QuestRewardOther import QuestRewardOther
    from db.models_generated.Item import Item
    from db.models_generated.Stain import Stain
    from db.models_generated.Emote import Emote
    from db.models_generated.Action import Action
    from db.models_generated.GeneralAction import GeneralAction
    from db.models_generated.PlaceName import PlaceName
    from db.models_generated.JournalGenre import JournalGenre
    from db.models_generated.EventIconType import EventIconType


class Quest(SQLModel, table=True):
    __tablename__ = "quest"
    __table_args__ = {'extend_existing': True}
    __allow_unmapped__ = True
    id: int = Field(default=None, primary_key=True)
    name: str
    param_id: str
    expansion_id: Optional[int] = Field(default=None, foreign_key="ex_version.id")
    expansion: Optional["ExVersion"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.expansion_id]"})
    class_job_category0_id: Optional[int] = Field(default=None, foreign_key="class_job_category.id")
    class_job_category0: Optional["ClassJobCategory"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.class_job_category0_id]"})
    class_job_level0: int
    quest_level_offset: int
    class_job_category1_id: Optional[int] = Field(default=None, foreign_key="class_job_category.id")
    class_job_category1: Optional["ClassJobCategory"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.class_job_category1_id]"})
    class_job_level1: int
    previous_quest_join: int
    previous_quest0_id: Optional[int] = Field(default=None, foreign_key="quest.id")
    previous_quest0: Optional["Quest"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.previous_quest0_id]"})
    previous_quest1_id: Optional[int] = Field(default=None, foreign_key="quest.id")
    previous_quest1: Optional["Quest"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.previous_quest1_id]"})
    previous_quest2_id: Optional[int] = Field(default=None, foreign_key="quest.id")
    previous_quest2: Optional["Quest"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.previous_quest2_id]"})
    quest_lock_join: int
    quest_lock0_id: Optional[int] = Field(default=None, foreign_key="quest.id")
    quest_lock0: Optional["Quest"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.quest_lock0_id]"})
    quest_lock1_id: Optional[int] = Field(default=None, foreign_key="quest.id")
    quest_lock1: Optional["Quest"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.quest_lock1_id]"})
    header: int
    class_job_unlock_id: Optional[int] = Field(default=None, foreign_key="class_job.id")
    class_job_unlock: Optional["ClassJob"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.class_job_unlock_id]"})
    grand_company_id: Optional[int] = Field(default=None, foreign_key="grand_company.id")
    grand_company: Optional["GrandCompany"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.grand_company_id]"})
    grand_company_rank_id: Optional[int] = Field(default=None, foreign_key="grand_company_rank.id")
    grand_company_rank: Optional["GrandCompanyRank"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.grand_company_rank_id]"})
    instance_content_join: int
    instance_content0_id: Optional[int] = Field(default=None, foreign_key="instance_content.id")
    instance_content0: Optional["InstanceContent"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.instance_content0_id]"})
    instance_content1_id: Optional[int] = Field(default=None, foreign_key="instance_content.id")
    instance_content1: Optional["InstanceContent"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.instance_content1_id]"})
    instance_content2_id: Optional[int] = Field(default=None, foreign_key="instance_content.id")
    instance_content2: Optional["InstanceContent"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.instance_content2_id]"})
    festival_id: Optional[int] = Field(default=None, foreign_key="festival.id")
    festival: Optional["Festival"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.festival_id]"})
    festival_begin: int
    festival_end: int
    bell_start: int
    bell_end: int
    beast_tribe_id: Optional[int] = Field(default=None, foreign_key="beast_tribe.id")
    beast_tribe: Optional["BeastTribe"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.beast_tribe_id]"})
    beast_reputation_rank_id: Optional[int] = Field(default=None, foreign_key="beast_reputation_rank.id")
    beast_reputation_rank: Optional["BeastReputationRank"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.beast_reputation_rank_id]"})
    beast_reputation_value: int
    satisfaction_npc_id: Optional[int] = Field(default=None, foreign_key="satisfaction_npc.id")
    satisfaction_npc: Optional["SatisfactionNpc"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.satisfaction_npc_id]"})
    satisfaction_level: int
    mount_required_id: Optional[int] = Field(default=None, foreign_key="mount.id")
    mount_required: Optional["Mount"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.mount_required_id]"})
    is_house_required: bool
    delivery_quest_id: Optional[int] = Field(default=None, foreign_key="delivery_quest.id")
    delivery_quest: Optional["DeliveryQuest"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.delivery_quest_id]"})
    issuer_start: int
    issuer_location_id: Optional[int] = Field(default=None, foreign_key="level.id")
    issuer_location: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.issuer_location_id]"})
    client_behavior_id: Optional[int] = Field(default=None, foreign_key="behavior.id")
    client_behavior: Optional["Behavior"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.client_behavior_id]"})
    target_end: int
    is_repeatable: bool
    repeat_interval_type: int
    quest_repeat_flag_id: Optional[int] = Field(default=None, foreign_key="quest_repeat_flag.id")
    quest_repeat_flag: Optional["QuestRepeatFlag"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.quest_repeat_flag_id]"})
    can_cancel: bool
    type: int
    quest_class_job_supply_id: Optional[int] = Field(default=None, foreign_key="quest_class_job_supply.id")
    quest_class_job_supply: Optional["QuestClassJobSupply"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.quest_class_job_supply_id]"})
    script_instruction0: str
    script_instruction1: str
    script_instruction2: str
    script_instruction3: str
    script_instruction4: str
    script_instruction5: str
    script_instruction6: str
    script_instruction7: str
    script_instruction8: str
    script_instruction9: str
    script_instruction10: str
    script_instruction11: str
    script_instruction12: str
    script_instruction13: str
    script_instruction14: str
    script_instruction15: str
    script_instruction16: str
    script_instruction17: str
    script_instruction18: str
    script_instruction19: str
    script_instruction20: str
    script_instruction21: str
    script_instruction22: str
    script_instruction23: str
    script_instruction24: str
    script_instruction25: str
    script_instruction26: str
    script_instruction27: str
    script_instruction28: str
    script_instruction29: str
    script_instruction30: str
    script_instruction31: str
    script_instruction32: str
    script_instruction33: str
    script_instruction34: str
    script_instruction35: str
    script_instruction36: str
    script_instruction37: str
    script_instruction38: str
    script_instruction39: str
    script_instruction40: str
    script_instruction41: str
    script_instruction42: str
    script_instruction43: str
    script_instruction44: str
    script_instruction45: str
    script_instruction46: str
    script_instruction47: str
    script_instruction48: str
    script_instruction49: str
    script_arg0: int
    script_arg1: int
    script_arg2: int
    script_arg3: int
    script_arg4: int
    script_arg5: int
    script_arg6: int
    script_arg7: int
    script_arg8: int
    script_arg9: int
    script_arg10: int
    script_arg11: int
    script_arg12: int
    script_arg13: int
    script_arg14: int
    script_arg15: int
    script_arg16: int
    script_arg17: int
    script_arg18: int
    script_arg19: int
    script_arg20: int
    script_arg21: int
    script_arg22: int
    script_arg23: int
    script_arg24: int
    script_arg25: int
    script_arg26: int
    script_arg27: int
    script_arg28: int
    script_arg29: int
    script_arg30: int
    script_arg31: int
    script_arg32: int
    script_arg33: int
    script_arg34: int
    script_arg35: int
    script_arg36: int
    script_arg37: int
    script_arg38: int
    script_arg39: int
    script_arg40: int
    script_arg41: int
    script_arg42: int
    script_arg43: int
    script_arg44: int
    script_arg45: int
    script_arg46: int
    script_arg47: int
    script_arg48: int
    script_arg49: int
    actor_spawn_seq0: int
    actor_spawn_seq1: int
    actor_spawn_seq2: int
    actor_spawn_seq3: int
    actor_spawn_seq4: int
    actor_spawn_seq5: int
    actor_spawn_seq6: int
    actor_spawn_seq7: int
    actor_spawn_seq8: int
    actor_spawn_seq9: int
    actor_spawn_seq10: int
    actor_spawn_seq11: int
    actor_spawn_seq12: int
    actor_spawn_seq13: int
    actor_spawn_seq14: int
    actor_spawn_seq15: int
    actor_spawn_seq16: int
    actor_spawn_seq17: int
    actor_spawn_seq18: int
    actor_spawn_seq19: int
    actor_spawn_seq20: int
    actor_spawn_seq21: int
    actor_spawn_seq22: int
    actor_spawn_seq23: int
    actor_spawn_seq24: int
    actor_spawn_seq25: int
    actor_spawn_seq26: int
    actor_spawn_seq27: int
    actor_spawn_seq28: int
    actor_spawn_seq29: int
    actor_spawn_seq30: int
    actor_spawn_seq31: int
    actor_spawn_seq32: int
    actor_spawn_seq33: int
    actor_spawn_seq34: int
    actor_spawn_seq35: int
    actor_spawn_seq36: int
    actor_spawn_seq37: int
    actor_spawn_seq38: int
    actor_spawn_seq39: int
    actor_spawn_seq40: int
    actor_spawn_seq41: int
    actor_spawn_seq42: int
    actor_spawn_seq43: int
    actor_spawn_seq44: int
    actor_spawn_seq45: int
    actor_spawn_seq46: int
    actor_spawn_seq47: int
    actor_spawn_seq48: int
    actor_spawn_seq49: int
    actor_spawn_seq50: int
    actor_spawn_seq51: int
    actor_spawn_seq52: int
    actor_spawn_seq53: int
    actor_spawn_seq54: int
    actor_spawn_seq55: int
    actor_spawn_seq56: int
    actor_spawn_seq57: int
    actor_spawn_seq58: int
    actor_spawn_seq59: int
    actor_spawn_seq60: int
    actor_spawn_seq61: int
    actor_spawn_seq62: int
    actor_spawn_seq63: int
    actor_despawn_seq0: int
    actor_despawn_seq1: int
    actor_despawn_seq2: int
    actor_despawn_seq3: int
    actor_despawn_seq4: int
    actor_despawn_seq5: int
    actor_despawn_seq6: int
    actor_despawn_seq7: int
    actor_despawn_seq8: int
    actor_despawn_seq9: int
    actor_despawn_seq10: int
    actor_despawn_seq11: int
    actor_despawn_seq12: int
    actor_despawn_seq13: int
    actor_despawn_seq14: int
    actor_despawn_seq15: int
    actor_despawn_seq16: int
    actor_despawn_seq17: int
    actor_despawn_seq18: int
    actor_despawn_seq19: int
    actor_despawn_seq20: int
    actor_despawn_seq21: int
    actor_despawn_seq22: int
    actor_despawn_seq23: int
    actor_despawn_seq24: int
    actor_despawn_seq25: int
    actor_despawn_seq26: int
    actor_despawn_seq27: int
    actor_despawn_seq28: int
    actor_despawn_seq29: int
    actor_despawn_seq30: int
    actor_despawn_seq31: int
    actor_despawn_seq32: int
    actor_despawn_seq33: int
    actor_despawn_seq34: int
    actor_despawn_seq35: int
    actor_despawn_seq36: int
    actor_despawn_seq37: int
    actor_despawn_seq38: int
    actor_despawn_seq39: int
    actor_despawn_seq40: int
    actor_despawn_seq41: int
    actor_despawn_seq42: int
    actor_despawn_seq43: int
    actor_despawn_seq44: int
    actor_despawn_seq45: int
    actor_despawn_seq46: int
    actor_despawn_seq47: int
    actor_despawn_seq48: int
    actor_despawn_seq49: int
    actor_despawn_seq50: int
    actor_despawn_seq51: int
    actor_despawn_seq52: int
    actor_despawn_seq53: int
    actor_despawn_seq54: int
    actor_despawn_seq55: int
    actor_despawn_seq56: int
    actor_despawn_seq57: int
    actor_despawn_seq58: int
    actor_despawn_seq59: int
    actor_despawn_seq60: int
    actor_despawn_seq61: int
    actor_despawn_seq62: int
    actor_despawn_seq63: int
    listener0: int
    listener1: int
    listener2: int
    listener3: int
    listener4: int
    listener5: int
    listener6: int
    listener7: int
    listener8: int
    listener9: int
    listener10: int
    listener11: int
    listener12: int
    listener13: int
    listener14: int
    listener15: int
    listener16: int
    listener17: int
    listener18: int
    listener19: int
    listener20: int
    listener21: int
    listener22: int
    listener23: int
    listener24: int
    listener25: int
    listener26: int
    listener27: int
    listener28: int
    listener29: int
    listener30: int
    listener31: int
    listener32: int
    listener33: int
    listener34: int
    listener35: int
    listener36: int
    listener37: int
    listener38: int
    listener39: int
    listener40: int
    listener41: int
    listener42: int
    listener43: int
    listener44: int
    listener45: int
    listener46: int
    listener47: int
    listener48: int
    listener49: int
    listener50: int
    listener51: int
    listener52: int
    listener53: int
    listener54: int
    listener55: int
    listener56: int
    listener57: int
    listener58: int
    listener59: int
    listener60: int
    listener61: int
    listener62: int
    listener63: int
    quest_u_int8_a0: int
    quest_u_int8_a1: int
    quest_u_int8_a2: int
    quest_u_int8_a3: int
    quest_u_int8_a4: int
    quest_u_int8_a5: int
    quest_u_int8_a6: int
    quest_u_int8_a7: int
    quest_u_int8_a8: int
    quest_u_int8_a9: int
    quest_u_int8_a10: int
    quest_u_int8_a11: int
    quest_u_int8_a12: int
    quest_u_int8_a13: int
    quest_u_int8_a14: int
    quest_u_int8_a15: int
    quest_u_int8_a16: int
    quest_u_int8_a17: int
    quest_u_int8_a18: int
    quest_u_int8_a19: int
    quest_u_int8_a20: int
    quest_u_int8_a21: int
    quest_u_int8_a22: int
    quest_u_int8_a23: int
    quest_u_int8_a24: int
    quest_u_int8_a25: int
    quest_u_int8_a26: int
    quest_u_int8_a27: int
    quest_u_int8_a28: int
    quest_u_int8_a29: int
    quest_u_int8_a30: int
    quest_u_int8_a31: int
    quest_u_int8_b0: int
    quest_u_int8_b1: int
    quest_u_int8_b2: int
    quest_u_int8_b3: int
    quest_u_int8_b4: int
    quest_u_int8_b5: int
    quest_u_int8_b6: int
    quest_u_int8_b7: int
    quest_u_int8_b8: int
    quest_u_int8_b9: int
    quest_u_int8_b10: int
    quest_u_int8_b11: int
    quest_u_int8_b12: int
    quest_u_int8_b13: int
    quest_u_int8_b14: int
    quest_u_int8_b15: int
    quest_u_int8_b16: int
    quest_u_int8_b17: int
    quest_u_int8_b18: int
    quest_u_int8_b19: int
    quest_u_int8_b20: int
    quest_u_int8_b21: int
    quest_u_int8_b22: int
    quest_u_int8_b23: int
    quest_u_int8_b24: int
    quest_u_int8_b25: int
    quest_u_int8_b26: int
    quest_u_int8_b27: int
    quest_u_int8_b28: int
    quest_u_int8_b29: int
    quest_u_int8_b30: int
    quest_u_int8_b31: int
    condition_type0: int
    condition_type1: int
    condition_type2: int
    condition_type3: int
    condition_type4: int
    condition_type5: int
    condition_type6: int
    condition_type7: int
    condition_type8: int
    condition_type9: int
    condition_type10: int
    condition_type11: int
    condition_type12: int
    condition_type13: int
    condition_type14: int
    condition_type15: int
    condition_type16: int
    condition_type17: int
    condition_type18: int
    condition_type19: int
    condition_type20: int
    condition_type21: int
    condition_type22: int
    condition_type23: int
    condition_type24: int
    condition_type25: int
    condition_type26: int
    condition_type27: int
    condition_type28: int
    condition_type29: int
    condition_type30: int
    condition_type31: int
    condition_type32: int
    condition_type33: int
    condition_type34: int
    condition_type35: int
    condition_type36: int
    condition_type37: int
    condition_type38: int
    condition_type39: int
    condition_type40: int
    condition_type41: int
    condition_type42: int
    condition_type43: int
    condition_type44: int
    condition_type45: int
    condition_type46: int
    condition_type47: int
    condition_type48: int
    condition_type49: int
    condition_type50: int
    condition_type51: int
    condition_type52: int
    condition_type53: int
    condition_type54: int
    condition_type55: int
    condition_type56: int
    condition_type57: int
    condition_type58: int
    condition_type59: int
    condition_type60: int
    condition_type61: int
    condition_type62: int
    condition_type63: int
    condition_value0: int
    condition_value1: int
    condition_value2: int
    condition_value3: int
    condition_value4: int
    condition_value5: int
    condition_value6: int
    condition_value7: int
    condition_value8: int
    condition_value9: int
    condition_value10: int
    condition_value11: int
    condition_value12: int
    condition_value13: int
    condition_value14: int
    condition_value15: int
    condition_value16: int
    condition_value17: int
    condition_value18: int
    condition_value19: int
    condition_value20: int
    condition_value21: int
    condition_value22: int
    condition_value23: int
    condition_value24: int
    condition_value25: int
    condition_value26: int
    condition_value27: int
    condition_value28: int
    condition_value29: int
    condition_value30: int
    condition_value31: int
    condition_value32: int
    condition_value33: int
    condition_value34: int
    condition_value35: int
    condition_value36: int
    condition_value37: int
    condition_value38: int
    condition_value39: int
    condition_value40: int
    condition_value41: int
    condition_value42: int
    condition_value43: int
    condition_value44: int
    condition_value45: int
    condition_value46: int
    condition_value47: int
    condition_value48: int
    condition_value49: int
    condition_value50: int
    condition_value51: int
    condition_value52: int
    condition_value53: int
    condition_value54: int
    condition_value55: int
    condition_value56: int
    condition_value57: int
    condition_value58: int
    condition_value59: int
    condition_value60: int
    condition_value61: int
    condition_value62: int
    condition_value63: int
    condition_operator0: int
    condition_operator1: int
    condition_operator2: int
    condition_operator3: int
    condition_operator4: int
    condition_operator5: int
    condition_operator6: int
    condition_operator7: int
    condition_operator8: int
    condition_operator9: int
    condition_operator10: int
    condition_operator11: int
    condition_operator12: int
    condition_operator13: int
    condition_operator14: int
    condition_operator15: int
    condition_operator16: int
    condition_operator17: int
    condition_operator18: int
    condition_operator19: int
    condition_operator20: int
    condition_operator21: int
    condition_operator22: int
    condition_operator23: int
    condition_operator24: int
    condition_operator25: int
    condition_operator26: int
    condition_operator27: int
    condition_operator28: int
    condition_operator29: int
    condition_operator30: int
    condition_operator31: int
    condition_operator32: int
    condition_operator33: int
    condition_operator34: int
    condition_operator35: int
    condition_operator36: int
    condition_operator37: int
    condition_operator38: int
    condition_operator39: int
    condition_operator40: int
    condition_operator41: int
    condition_operator42: int
    condition_operator43: int
    condition_operator44: int
    condition_operator45: int
    condition_operator46: int
    condition_operator47: int
    condition_operator48: int
    condition_operator49: int
    condition_operator50: int
    condition_operator51: int
    condition_operator52: int
    condition_operator53: int
    condition_operator54: int
    condition_operator55: int
    condition_operator56: int
    condition_operator57: int
    condition_operator58: int
    condition_operator59: int
    condition_operator60: int
    condition_operator61: int
    condition_operator62: int
    condition_operator63: int
    behavior0: int
    behavior1: int
    behavior2: int
    behavior3: int
    behavior4: int
    behavior5: int
    behavior6: int
    behavior7: int
    behavior8: int
    behavior9: int
    behavior10: int
    behavior11: int
    behavior12: int
    behavior13: int
    behavior14: int
    behavior15: int
    behavior16: int
    behavior17: int
    behavior18: int
    behavior19: int
    behavior20: int
    behavior21: int
    behavior22: int
    behavior23: int
    behavior24: int
    behavior25: int
    behavior26: int
    behavior27: int
    behavior28: int
    behavior29: int
    behavior30: int
    behavior31: int
    behavior32: int
    behavior33: int
    behavior34: int
    behavior35: int
    behavior36: int
    behavior37: int
    behavior38: int
    behavior39: int
    behavior40: int
    behavior41: int
    behavior42: int
    behavior43: int
    behavior44: int
    behavior45: int
    behavior46: int
    behavior47: int
    behavior48: int
    behavior49: int
    behavior50: int
    behavior51: int
    behavior52: int
    behavior53: int
    behavior54: int
    behavior55: int
    behavior56: int
    behavior57: int
    behavior58: int
    behavior59: int
    behavior60: int
    behavior61: int
    behavior62: int
    behavior63: int
    visible_bool0: bool
    visible_bool1: bool
    visible_bool2: bool
    visible_bool3: bool
    visible_bool4: bool
    visible_bool5: bool
    visible_bool6: bool
    visible_bool7: bool
    visible_bool8: bool
    visible_bool9: bool
    visible_bool10: bool
    visible_bool11: bool
    visible_bool12: bool
    visible_bool13: bool
    visible_bool14: bool
    visible_bool15: bool
    visible_bool16: bool
    visible_bool17: bool
    visible_bool18: bool
    visible_bool19: bool
    visible_bool20: bool
    visible_bool21: bool
    visible_bool22: bool
    visible_bool23: bool
    visible_bool24: bool
    visible_bool25: bool
    visible_bool26: bool
    visible_bool27: bool
    visible_bool28: bool
    visible_bool29: bool
    visible_bool30: bool
    visible_bool31: bool
    visible_bool32: bool
    visible_bool33: bool
    visible_bool34: bool
    visible_bool35: bool
    visible_bool36: bool
    visible_bool37: bool
    visible_bool38: bool
    visible_bool39: bool
    visible_bool40: bool
    visible_bool41: bool
    visible_bool42: bool
    visible_bool43: bool
    visible_bool44: bool
    visible_bool45: bool
    visible_bool46: bool
    visible_bool47: bool
    visible_bool48: bool
    visible_bool49: bool
    visible_bool50: bool
    visible_bool51: bool
    visible_bool52: bool
    visible_bool53: bool
    visible_bool54: bool
    visible_bool55: bool
    visible_bool56: bool
    visible_bool57: bool
    visible_bool58: bool
    visible_bool59: bool
    visible_bool60: bool
    visible_bool61: bool
    visible_bool62: bool
    visible_bool63: bool
    condition_bool0: bool
    condition_bool1: bool
    condition_bool2: bool
    condition_bool3: bool
    condition_bool4: bool
    condition_bool5: bool
    condition_bool6: bool
    condition_bool7: bool
    condition_bool8: bool
    condition_bool9: bool
    condition_bool10: bool
    condition_bool11: bool
    condition_bool12: bool
    condition_bool13: bool
    condition_bool14: bool
    condition_bool15: bool
    condition_bool16: bool
    condition_bool17: bool
    condition_bool18: bool
    condition_bool19: bool
    condition_bool20: bool
    condition_bool21: bool
    condition_bool22: bool
    condition_bool23: bool
    condition_bool24: bool
    condition_bool25: bool
    condition_bool26: bool
    condition_bool27: bool
    condition_bool28: bool
    condition_bool29: bool
    condition_bool30: bool
    condition_bool31: bool
    condition_bool32: bool
    condition_bool33: bool
    condition_bool34: bool
    condition_bool35: bool
    condition_bool36: bool
    condition_bool37: bool
    condition_bool38: bool
    condition_bool39: bool
    condition_bool40: bool
    condition_bool41: bool
    condition_bool42: bool
    condition_bool43: bool
    condition_bool44: bool
    condition_bool45: bool
    condition_bool46: bool
    condition_bool47: bool
    condition_bool48: bool
    condition_bool49: bool
    condition_bool50: bool
    condition_bool51: bool
    condition_bool52: bool
    condition_bool53: bool
    condition_bool54: bool
    condition_bool55: bool
    condition_bool56: bool
    condition_bool57: bool
    condition_bool58: bool
    condition_bool59: bool
    condition_bool60: bool
    condition_bool61: bool
    condition_bool62: bool
    condition_bool63: bool
    item_bool0: bool
    item_bool1: bool
    item_bool2: bool
    item_bool3: bool
    item_bool4: bool
    item_bool5: bool
    item_bool6: bool
    item_bool7: bool
    item_bool8: bool
    item_bool9: bool
    item_bool10: bool
    item_bool11: bool
    item_bool12: bool
    item_bool13: bool
    item_bool14: bool
    item_bool15: bool
    item_bool16: bool
    item_bool17: bool
    item_bool18: bool
    item_bool19: bool
    item_bool20: bool
    item_bool21: bool
    item_bool22: bool
    item_bool23: bool
    item_bool24: bool
    item_bool25: bool
    item_bool26: bool
    item_bool27: bool
    item_bool28: bool
    item_bool29: bool
    item_bool30: bool
    item_bool31: bool
    item_bool32: bool
    item_bool33: bool
    item_bool34: bool
    item_bool35: bool
    item_bool36: bool
    item_bool37: bool
    item_bool38: bool
    item_bool39: bool
    item_bool40: bool
    item_bool41: bool
    item_bool42: bool
    item_bool43: bool
    item_bool44: bool
    item_bool45: bool
    item_bool46: bool
    item_bool47: bool
    item_bool48: bool
    item_bool49: bool
    item_bool50: bool
    item_bool51: bool
    item_bool52: bool
    item_bool53: bool
    item_bool54: bool
    item_bool55: bool
    item_bool56: bool
    item_bool57: bool
    item_bool58: bool
    item_bool59: bool
    item_bool60: bool
    item_bool61: bool
    item_bool62: bool
    item_bool63: bool
    announce_bool0: bool
    announce_bool1: bool
    announce_bool2: bool
    announce_bool3: bool
    announce_bool4: bool
    announce_bool5: bool
    announce_bool6: bool
    announce_bool7: bool
    announce_bool8: bool
    announce_bool9: bool
    announce_bool10: bool
    announce_bool11: bool
    announce_bool12: bool
    announce_bool13: bool
    announce_bool14: bool
    announce_bool15: bool
    announce_bool16: bool
    announce_bool17: bool
    announce_bool18: bool
    announce_bool19: bool
    announce_bool20: bool
    announce_bool21: bool
    announce_bool22: bool
    announce_bool23: bool
    announce_bool24: bool
    announce_bool25: bool
    announce_bool26: bool
    announce_bool27: bool
    announce_bool28: bool
    announce_bool29: bool
    announce_bool30: bool
    announce_bool31: bool
    announce_bool32: bool
    announce_bool33: bool
    announce_bool34: bool
    announce_bool35: bool
    announce_bool36: bool
    announce_bool37: bool
    announce_bool38: bool
    announce_bool39: bool
    announce_bool40: bool
    announce_bool41: bool
    announce_bool42: bool
    announce_bool43: bool
    announce_bool44: bool
    announce_bool45: bool
    announce_bool46: bool
    announce_bool47: bool
    announce_bool48: bool
    announce_bool49: bool
    announce_bool50: bool
    announce_bool51: bool
    announce_bool52: bool
    announce_bool53: bool
    announce_bool54: bool
    announce_bool55: bool
    announce_bool56: bool
    announce_bool57: bool
    announce_bool58: bool
    announce_bool59: bool
    announce_bool60: bool
    announce_bool61: bool
    announce_bool62: bool
    announce_bool63: bool
    behavior_bool0: bool
    behavior_bool1: bool
    behavior_bool2: bool
    behavior_bool3: bool
    behavior_bool4: bool
    behavior_bool5: bool
    behavior_bool6: bool
    behavior_bool7: bool
    behavior_bool8: bool
    behavior_bool9: bool
    behavior_bool10: bool
    behavior_bool11: bool
    behavior_bool12: bool
    behavior_bool13: bool
    behavior_bool14: bool
    behavior_bool15: bool
    behavior_bool16: bool
    behavior_bool17: bool
    behavior_bool18: bool
    behavior_bool19: bool
    behavior_bool20: bool
    behavior_bool21: bool
    behavior_bool22: bool
    behavior_bool23: bool
    behavior_bool24: bool
    behavior_bool25: bool
    behavior_bool26: bool
    behavior_bool27: bool
    behavior_bool28: bool
    behavior_bool29: bool
    behavior_bool30: bool
    behavior_bool31: bool
    behavior_bool32: bool
    behavior_bool33: bool
    behavior_bool34: bool
    behavior_bool35: bool
    behavior_bool36: bool
    behavior_bool37: bool
    behavior_bool38: bool
    behavior_bool39: bool
    behavior_bool40: bool
    behavior_bool41: bool
    behavior_bool42: bool
    behavior_bool43: bool
    behavior_bool44: bool
    behavior_bool45: bool
    behavior_bool46: bool
    behavior_bool47: bool
    behavior_bool48: bool
    behavior_bool49: bool
    behavior_bool50: bool
    behavior_bool51: bool
    behavior_bool52: bool
    behavior_bool53: bool
    behavior_bool54: bool
    behavior_bool55: bool
    behavior_bool56: bool
    behavior_bool57: bool
    behavior_bool58: bool
    behavior_bool59: bool
    behavior_bool60: bool
    behavior_bool61: bool
    behavior_bool62: bool
    behavior_bool63: bool
    accept_bool0: bool
    accept_bool1: bool
    accept_bool2: bool
    accept_bool3: bool
    accept_bool4: bool
    accept_bool5: bool
    accept_bool6: bool
    accept_bool7: bool
    accept_bool8: bool
    accept_bool9: bool
    accept_bool10: bool
    accept_bool11: bool
    accept_bool12: bool
    accept_bool13: bool
    accept_bool14: bool
    accept_bool15: bool
    accept_bool16: bool
    accept_bool17: bool
    accept_bool18: bool
    accept_bool19: bool
    accept_bool20: bool
    accept_bool21: bool
    accept_bool22: bool
    accept_bool23: bool
    accept_bool24: bool
    accept_bool25: bool
    accept_bool26: bool
    accept_bool27: bool
    accept_bool28: bool
    accept_bool29: bool
    accept_bool30: bool
    accept_bool31: bool
    accept_bool32: bool
    accept_bool33: bool
    accept_bool34: bool
    accept_bool35: bool
    accept_bool36: bool
    accept_bool37: bool
    accept_bool38: bool
    accept_bool39: bool
    accept_bool40: bool
    accept_bool41: bool
    accept_bool42: bool
    accept_bool43: bool
    accept_bool44: bool
    accept_bool45: bool
    accept_bool46: bool
    accept_bool47: bool
    accept_bool48: bool
    accept_bool49: bool
    accept_bool50: bool
    accept_bool51: bool
    accept_bool52: bool
    accept_bool53: bool
    accept_bool54: bool
    accept_bool55: bool
    accept_bool56: bool
    accept_bool57: bool
    accept_bool58: bool
    accept_bool59: bool
    accept_bool60: bool
    accept_bool61: bool
    accept_bool62: bool
    accept_bool63: bool
    qualified_bool0: bool
    qualified_bool1: bool
    qualified_bool2: bool
    qualified_bool3: bool
    qualified_bool4: bool
    qualified_bool5: bool
    qualified_bool6: bool
    qualified_bool7: bool
    qualified_bool8: bool
    qualified_bool9: bool
    qualified_bool10: bool
    qualified_bool11: bool
    qualified_bool12: bool
    qualified_bool13: bool
    qualified_bool14: bool
    qualified_bool15: bool
    qualified_bool16: bool
    qualified_bool17: bool
    qualified_bool18: bool
    qualified_bool19: bool
    qualified_bool20: bool
    qualified_bool21: bool
    qualified_bool22: bool
    qualified_bool23: bool
    qualified_bool24: bool
    qualified_bool25: bool
    qualified_bool26: bool
    qualified_bool27: bool
    qualified_bool28: bool
    qualified_bool29: bool
    qualified_bool30: bool
    qualified_bool31: bool
    qualified_bool32: bool
    qualified_bool33: bool
    qualified_bool34: bool
    qualified_bool35: bool
    qualified_bool36: bool
    qualified_bool37: bool
    qualified_bool38: bool
    qualified_bool39: bool
    qualified_bool40: bool
    qualified_bool41: bool
    qualified_bool42: bool
    qualified_bool43: bool
    qualified_bool44: bool
    qualified_bool45: bool
    qualified_bool46: bool
    qualified_bool47: bool
    qualified_bool48: bool
    qualified_bool49: bool
    qualified_bool50: bool
    qualified_bool51: bool
    qualified_bool52: bool
    qualified_bool53: bool
    qualified_bool54: bool
    qualified_bool55: bool
    qualified_bool56: bool
    qualified_bool57: bool
    qualified_bool58: bool
    qualified_bool59: bool
    qualified_bool60: bool
    qualified_bool61: bool
    qualified_bool62: bool
    qualified_bool63: bool
    can_target_bool0: bool
    can_target_bool1: bool
    can_target_bool2: bool
    can_target_bool3: bool
    can_target_bool4: bool
    can_target_bool5: bool
    can_target_bool6: bool
    can_target_bool7: bool
    can_target_bool8: bool
    can_target_bool9: bool
    can_target_bool10: bool
    can_target_bool11: bool
    can_target_bool12: bool
    can_target_bool13: bool
    can_target_bool14: bool
    can_target_bool15: bool
    can_target_bool16: bool
    can_target_bool17: bool
    can_target_bool18: bool
    can_target_bool19: bool
    can_target_bool20: bool
    can_target_bool21: bool
    can_target_bool22: bool
    can_target_bool23: bool
    can_target_bool24: bool
    can_target_bool25: bool
    can_target_bool26: bool
    can_target_bool27: bool
    can_target_bool28: bool
    can_target_bool29: bool
    can_target_bool30: bool
    can_target_bool31: bool
    can_target_bool32: bool
    can_target_bool33: bool
    can_target_bool34: bool
    can_target_bool35: bool
    can_target_bool36: bool
    can_target_bool37: bool
    can_target_bool38: bool
    can_target_bool39: bool
    can_target_bool40: bool
    can_target_bool41: bool
    can_target_bool42: bool
    can_target_bool43: bool
    can_target_bool44: bool
    can_target_bool45: bool
    can_target_bool46: bool
    can_target_bool47: bool
    can_target_bool48: bool
    can_target_bool49: bool
    can_target_bool50: bool
    can_target_bool51: bool
    can_target_bool52: bool
    can_target_bool53: bool
    can_target_bool54: bool
    can_target_bool55: bool
    can_target_bool56: bool
    can_target_bool57: bool
    can_target_bool58: bool
    can_target_bool59: bool
    can_target_bool60: bool
    can_target_bool61: bool
    can_target_bool62: bool
    can_target_bool63: bool
    to_do_complete_seq0: int
    to_do_complete_seq1: int
    to_do_complete_seq2: int
    to_do_complete_seq3: int
    to_do_complete_seq4: int
    to_do_complete_seq5: int
    to_do_complete_seq6: int
    to_do_complete_seq7: int
    to_do_complete_seq8: int
    to_do_complete_seq9: int
    to_do_complete_seq10: int
    to_do_complete_seq11: int
    to_do_complete_seq12: int
    to_do_complete_seq13: int
    to_do_complete_seq14: int
    to_do_complete_seq15: int
    to_do_complete_seq16: int
    to_do_complete_seq17: int
    to_do_complete_seq18: int
    to_do_complete_seq19: int
    to_do_complete_seq20: int
    to_do_complete_seq21: int
    to_do_complete_seq22: int
    to_do_complete_seq23: int
    to_do_qty0: int
    to_do_qty1: int
    to_do_qty2: int
    to_do_qty3: int
    to_do_qty4: int
    to_do_qty5: int
    to_do_qty6: int
    to_do_qty7: int
    to_do_qty8: int
    to_do_qty9: int
    to_do_qty10: int
    to_do_qty11: int
    to_do_qty12: int
    to_do_qty13: int
    to_do_qty14: int
    to_do_qty15: int
    to_do_qty16: int
    to_do_qty17: int
    to_do_qty18: int
    to_do_qty19: int
    to_do_qty20: int
    to_do_qty21: int
    to_do_qty22: int
    to_do_qty23: int
    to_do_location00_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location00: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location00_id]"})
    to_do_location10_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location10: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location10_id]"})
    to_do_location20_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location20: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location20_id]"})
    to_do_location30_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location30: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location30_id]"})
    to_do_location40_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location40: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location40_id]"})
    to_do_location50_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location50: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location50_id]"})
    to_do_location60_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location60: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location60_id]"})
    to_do_location70_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location70: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location70_id]"})
    to_do_location80_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location80: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location80_id]"})
    to_do_location90_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location90: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location90_id]"})
    to_do_location100_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location100: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location100_id]"})
    to_do_location110_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location110: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location110_id]"})
    to_do_location120_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location120: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location120_id]"})
    to_do_location130_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location130: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location130_id]"})
    to_do_location140_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location140: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location140_id]"})
    to_do_location150_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location150: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location150_id]"})
    to_do_location160_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location160: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location160_id]"})
    to_do_location170_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location170: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location170_id]"})
    to_do_location180_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location180: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location180_id]"})
    to_do_location190_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location190: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location190_id]"})
    to_do_location200_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location200: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location200_id]"})
    to_do_location210_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location210: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location210_id]"})
    to_do_location220_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location220: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location220_id]"})
    to_do_location230_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location230: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location230_id]"})
    to_do_location01_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location01: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location01_id]"})
    to_do_location11_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location11: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location11_id]"})
    to_do_location21_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location21: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location21_id]"})
    to_do_location31_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location31: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location31_id]"})
    to_do_location41_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location41: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location41_id]"})
    to_do_location51_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location51: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location51_id]"})
    to_do_location61_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location61: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location61_id]"})
    to_do_location71_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location71: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location71_id]"})
    to_do_location81_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location81: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location81_id]"})
    to_do_location91_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location91: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location91_id]"})
    to_do_location101_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location101: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location101_id]"})
    to_do_location111_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location111: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location111_id]"})
    to_do_location121_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location121: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location121_id]"})
    to_do_location131_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location131: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location131_id]"})
    to_do_location141_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location141: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location141_id]"})
    to_do_location151_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location151: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location151_id]"})
    to_do_location161_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location161: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location161_id]"})
    to_do_location171_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location171: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location171_id]"})
    to_do_location181_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location181: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location181_id]"})
    to_do_location191_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location191: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location191_id]"})
    to_do_location201_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location201: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location201_id]"})
    to_do_location211_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location211: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location211_id]"})
    to_do_location221_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location221: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location221_id]"})
    to_do_location231_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location231: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location231_id]"})
    to_do_location02_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location02: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location02_id]"})
    to_do_location12_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location12: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location12_id]"})
    to_do_location22_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location22: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location22_id]"})
    to_do_location32_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location32: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location32_id]"})
    to_do_location42_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location42: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location42_id]"})
    to_do_location52_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location52: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location52_id]"})
    to_do_location62_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location62: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location62_id]"})
    to_do_location72_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location72: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location72_id]"})
    to_do_location82_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location82: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location82_id]"})
    to_do_location92_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location92: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location92_id]"})
    to_do_location102_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location102: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location102_id]"})
    to_do_location112_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location112: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location112_id]"})
    to_do_location122_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location122: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location122_id]"})
    to_do_location132_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location132: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location132_id]"})
    to_do_location142_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location142: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location142_id]"})
    to_do_location152_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location152: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location152_id]"})
    to_do_location162_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location162: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location162_id]"})
    to_do_location172_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location172: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location172_id]"})
    to_do_location182_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location182: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location182_id]"})
    to_do_location192_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location192: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location192_id]"})
    to_do_location202_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location202: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location202_id]"})
    to_do_location212_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location212: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location212_id]"})
    to_do_location222_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location222: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location222_id]"})
    to_do_location232_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location232: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location232_id]"})
    to_do_location03_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location03: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location03_id]"})
    to_do_location13_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location13: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location13_id]"})
    to_do_location23_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location23: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location23_id]"})
    to_do_location33_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location33: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location33_id]"})
    to_do_location43_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location43: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location43_id]"})
    to_do_location53_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location53: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location53_id]"})
    to_do_location63_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location63: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location63_id]"})
    to_do_location73_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location73: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location73_id]"})
    to_do_location83_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location83: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location83_id]"})
    to_do_location93_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location93: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location93_id]"})
    to_do_location103_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location103: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location103_id]"})
    to_do_location113_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location113: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location113_id]"})
    to_do_location123_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location123: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location123_id]"})
    to_do_location133_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location133: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location133_id]"})
    to_do_location143_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location143: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location143_id]"})
    to_do_location153_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location153: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location153_id]"})
    to_do_location163_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location163: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location163_id]"})
    to_do_location173_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location173: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location173_id]"})
    to_do_location183_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location183: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location183_id]"})
    to_do_location193_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location193: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location193_id]"})
    to_do_location203_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location203: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location203_id]"})
    to_do_location213_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location213: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location213_id]"})
    to_do_location223_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location223: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location223_id]"})
    to_do_location233_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location233: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location233_id]"})
    to_do_location04_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location04: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location04_id]"})
    to_do_location14_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location14: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location14_id]"})
    to_do_location24_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location24: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location24_id]"})
    to_do_location34_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location34: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location34_id]"})
    to_do_location44_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location44: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location44_id]"})
    to_do_location54_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location54: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location54_id]"})
    to_do_location64_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location64: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location64_id]"})
    to_do_location74_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location74: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location74_id]"})
    to_do_location84_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location84: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location84_id]"})
    to_do_location94_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location94: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location94_id]"})
    to_do_location104_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location104: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location104_id]"})
    to_do_location114_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location114: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location114_id]"})
    to_do_location124_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location124: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location124_id]"})
    to_do_location134_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location134: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location134_id]"})
    to_do_location144_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location144: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location144_id]"})
    to_do_location154_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location154: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location154_id]"})
    to_do_location164_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location164: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location164_id]"})
    to_do_location174_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location174: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location174_id]"})
    to_do_location184_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location184: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location184_id]"})
    to_do_location194_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location194: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location194_id]"})
    to_do_location204_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location204: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location204_id]"})
    to_do_location214_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location214: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location214_id]"})
    to_do_location224_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location224: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location224_id]"})
    to_do_location234_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location234: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location234_id]"})
    to_do_location05_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location05: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location05_id]"})
    to_do_location15_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location15: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location15_id]"})
    to_do_location25_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location25: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location25_id]"})
    to_do_location35_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location35: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location35_id]"})
    to_do_location45_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location45: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location45_id]"})
    to_do_location55_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location55: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location55_id]"})
    to_do_location65_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location65: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location65_id]"})
    to_do_location75_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location75: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location75_id]"})
    to_do_location85_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location85: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location85_id]"})
    to_do_location95_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location95: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location95_id]"})
    to_do_location105_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location105: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location105_id]"})
    to_do_location115_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location115: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location115_id]"})
    to_do_location125_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location125: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location125_id]"})
    to_do_location135_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location135: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location135_id]"})
    to_do_location145_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location145: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location145_id]"})
    to_do_location155_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location155: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location155_id]"})
    to_do_location165_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location165: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location165_id]"})
    to_do_location175_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location175: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location175_id]"})
    to_do_location185_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location185: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location185_id]"})
    to_do_location195_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location195: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location195_id]"})
    to_do_location205_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location205: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location205_id]"})
    to_do_location215_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location215: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location215_id]"})
    to_do_location225_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location225: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location225_id]"})
    to_do_location235_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location235: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location235_id]"})
    to_do_location06_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location06: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location06_id]"})
    to_do_location16_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location16: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location16_id]"})
    to_do_location26_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location26: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location26_id]"})
    to_do_location36_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location36: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location36_id]"})
    to_do_location46_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location46: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location46_id]"})
    to_do_location56_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location56: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location56_id]"})
    to_do_location66_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location66: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location66_id]"})
    to_do_location76_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location76: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location76_id]"})
    to_do_location86_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location86: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location86_id]"})
    to_do_location96_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location96: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location96_id]"})
    to_do_location106_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location106: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location106_id]"})
    to_do_location116_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location116: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location116_id]"})
    to_do_location126_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location126: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location126_id]"})
    to_do_location136_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location136: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location136_id]"})
    to_do_location146_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location146: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location146_id]"})
    to_do_location156_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location156: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location156_id]"})
    to_do_location166_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location166: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location166_id]"})
    to_do_location176_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location176: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location176_id]"})
    to_do_location186_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location186: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location186_id]"})
    to_do_location196_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location196: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location196_id]"})
    to_do_location206_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location206: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location206_id]"})
    to_do_location216_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location216: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location216_id]"})
    to_do_location226_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location226: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location226_id]"})
    to_do_location236_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location236: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location236_id]"})
    to_do_location07_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location07: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location07_id]"})
    to_do_location17_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location17: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location17_id]"})
    to_do_location27_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location27: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location27_id]"})
    to_do_location37_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location37: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location37_id]"})
    to_do_location47_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location47: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location47_id]"})
    to_do_location57_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location57: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location57_id]"})
    to_do_location67_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location67: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location67_id]"})
    to_do_location77_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location77: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location77_id]"})
    to_do_location87_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location87: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location87_id]"})
    to_do_location97_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location97: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location97_id]"})
    to_do_location107_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location107: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location107_id]"})
    to_do_location117_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location117: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location117_id]"})
    to_do_location127_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location127: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location127_id]"})
    to_do_location137_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location137: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location137_id]"})
    to_do_location147_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location147: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location147_id]"})
    to_do_location157_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location157: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location157_id]"})
    to_do_location167_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location167: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location167_id]"})
    to_do_location177_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location177: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location177_id]"})
    to_do_location187_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location187: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location187_id]"})
    to_do_location197_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location197: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location197_id]"})
    to_do_location207_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location207: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location207_id]"})
    to_do_location217_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location217: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location217_id]"})
    to_do_location227_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location227: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location227_id]"})
    to_do_location237_id: Optional[int] = Field(default=None, foreign_key="level.id")
    to_do_location237: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.to_do_location237_id]"})
    countable_num0: int
    countable_num1: int
    countable_num2: int
    countable_num3: int
    countable_num4: int
    countable_num5: int
    countable_num6: int
    countable_num7: int
    countable_num8: int
    countable_num9: int
    countable_num10: int
    countable_num11: int
    countable_num12: int
    countable_num13: int
    countable_num14: int
    countable_num15: int
    countable_num16: int
    countable_num17: int
    countable_num18: int
    countable_num19: int
    countable_num20: int
    countable_num21: int
    countable_num22: int
    countable_num23: int
    level_max: int
    class_job_required_id: Optional[int] = Field(default=None, foreign_key="class_job.id")
    class_job_required: Optional["ClassJob"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.class_job_required_id]"})
    quest_reward_other_display_id: Optional[int] = Field(default=None, foreign_key="quest_reward_other.id")
    quest_reward_other_display: Optional["QuestRewardOther"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.quest_reward_other_display_id]"})
    exp_factor: int
    gil_reward: int
    currency_reward_id: Optional[int] = Field(default=None, foreign_key="item.id")
    currency_reward: Optional["Item"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.currency_reward_id]"})
    currency_reward_count: int
    item_catalyst0_id: Optional[int] = Field(default=None, foreign_key="item.id")
    item_catalyst0: Optional["Item"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.item_catalyst0_id]"})
    item_catalyst1_id: Optional[int] = Field(default=None, foreign_key="item.id")
    item_catalyst1: Optional["Item"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.item_catalyst1_id]"})
    item_catalyst2_id: Optional[int] = Field(default=None, foreign_key="item.id")
    item_catalyst2: Optional["Item"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.item_catalyst2_id]"})
    item_count_catalyst0: int
    item_count_catalyst1: int
    item_count_catalyst2: int
    item_reward_type: int
    item_reward0: int
    item_reward1: int
    item_reward2: int
    item_reward3: int
    item_reward4: int
    item_reward5: int
    item_reward6: int
    item_count_reward0: int
    item_count_reward1: int
    item_count_reward2: int
    item_count_reward3: int
    item_count_reward4: int
    item_count_reward5: int
    item_count_reward6: int
    stain_reward0_id: Optional[int] = Field(default=None, foreign_key="stain.id")
    stain_reward0: Optional["Stain"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.stain_reward0_id]"})
    stain_reward1_id: Optional[int] = Field(default=None, foreign_key="stain.id")
    stain_reward1: Optional["Stain"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.stain_reward1_id]"})
    stain_reward2_id: Optional[int] = Field(default=None, foreign_key="stain.id")
    stain_reward2: Optional["Stain"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.stain_reward2_id]"})
    stain_reward3_id: Optional[int] = Field(default=None, foreign_key="stain.id")
    stain_reward3: Optional["Stain"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.stain_reward3_id]"})
    stain_reward4_id: Optional[int] = Field(default=None, foreign_key="stain.id")
    stain_reward4: Optional["Stain"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.stain_reward4_id]"})
    stain_reward5_id: Optional[int] = Field(default=None, foreign_key="stain.id")
    stain_reward5: Optional["Stain"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.stain_reward5_id]"})
    stain_reward6_id: Optional[int] = Field(default=None, foreign_key="stain.id")
    stain_reward6: Optional["Stain"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.stain_reward6_id]"})
    optional_item_reward0_id: Optional[int] = Field(default=None, foreign_key="item.id")
    optional_item_reward0: Optional["Item"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.optional_item_reward0_id]"})
    optional_item_reward1_id: Optional[int] = Field(default=None, foreign_key="item.id")
    optional_item_reward1: Optional["Item"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.optional_item_reward1_id]"})
    optional_item_reward2_id: Optional[int] = Field(default=None, foreign_key="item.id")
    optional_item_reward2: Optional["Item"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.optional_item_reward2_id]"})
    optional_item_reward3_id: Optional[int] = Field(default=None, foreign_key="item.id")
    optional_item_reward3: Optional["Item"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.optional_item_reward3_id]"})
    optional_item_reward4_id: Optional[int] = Field(default=None, foreign_key="item.id")
    optional_item_reward4: Optional["Item"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.optional_item_reward4_id]"})
    optional_item_count_reward0: int
    optional_item_count_reward1: int
    optional_item_count_reward2: int
    optional_item_count_reward3: int
    optional_item_count_reward4: int
    optional_item_is_h_q_reward0: bool
    optional_item_is_h_q_reward1: bool
    optional_item_is_h_q_reward2: bool
    optional_item_is_h_q_reward3: bool
    optional_item_is_h_q_reward4: bool
    optional_item_stain_reward0_id: Optional[int] = Field(default=None, foreign_key="stain.id")
    optional_item_stain_reward0: Optional["Stain"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.optional_item_stain_reward0_id]"})
    optional_item_stain_reward1_id: Optional[int] = Field(default=None, foreign_key="stain.id")
    optional_item_stain_reward1: Optional["Stain"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.optional_item_stain_reward1_id]"})
    optional_item_stain_reward2_id: Optional[int] = Field(default=None, foreign_key="stain.id")
    optional_item_stain_reward2: Optional["Stain"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.optional_item_stain_reward2_id]"})
    optional_item_stain_reward3_id: Optional[int] = Field(default=None, foreign_key="stain.id")
    optional_item_stain_reward3: Optional["Stain"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.optional_item_stain_reward3_id]"})
    optional_item_stain_reward4_id: Optional[int] = Field(default=None, foreign_key="stain.id")
    optional_item_stain_reward4: Optional["Stain"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.optional_item_stain_reward4_id]"})
    emote_reward_id: Optional[int] = Field(default=None, foreign_key="emote.id")
    emote_reward: Optional["Emote"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.emote_reward_id]"})
    action_reward_id: Optional[int] = Field(default=None, foreign_key="action.id")
    action_reward: Optional["Action"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.action_reward_id]"})
    general_action_reward0_id: Optional[int] = Field(default=None, foreign_key="general_action.id")
    general_action_reward0: Optional["GeneralAction"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.general_action_reward0_id]"})
    general_action_reward1_id: Optional[int] = Field(default=None, foreign_key="general_action.id")
    general_action_reward1: Optional["GeneralAction"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.general_action_reward1_id]"})
    system_reward0: int
    other_reward_id: Optional[int] = Field(default=None, foreign_key="quest_reward_other.id")
    other_reward: Optional["QuestRewardOther"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.other_reward_id]"})
    system_reward1: int
    g_c_type_reward: int
    instance_content_unlock_id: Optional[int] = Field(default=None, foreign_key="instance_content.id")
    instance_content_unlock: Optional["InstanceContent"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.instance_content_unlock_id]"})
    tomestone: int
    tomestone_reward: int
    tomestone_count_reward: int
    reputation_reward: int
    place_name_id: Optional[int] = Field(default=None, foreign_key="place_name.id")
    place_name: Optional["PlaceName"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.place_name_id]"})
    journal_genre_id: Optional[int] = Field(default=None, foreign_key="journal_genre.id")
    journal_genre: Optional["JournalGenre"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.journal_genre_id]"})
    icon: str
    icon_special: str
    introduction: bool
    hide_offer_icon: bool
    event_icon_type_id: Optional[int] = Field(default=None, foreign_key="event_icon_type.id")
    event_icon_type: Optional["EventIconType"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Quest.event_icon_type_id]"})
    sort_key: int

