from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from db.models_generated.ClassJobCategory import ClassJobCategory
    from db.models_generated.Item import Item
    from db.models_generated.Town import Town
    from db.models_generated.MonsterNote import MonsterNote
    from db.models_generated.Action import Action
    from db.models_generated.Quest import Quest


class ClassJob(SQLModel, table=True):
    __tablename__ = "class_job"
    __table_args__ = {'extend_existing': True}
    __allow_unmapped__ = True
    id: int = Field(default=None, primary_key=True)
    name: str
    abbreviation: str
    class_job_category_id: Optional[int] = Field(default=None, foreign_key="class_job_category.id")
    class_job_category: Optional["ClassJobCategory"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[ClassJob.class_job_category_id]"})
    exp_array_index: int
    battle_class_index: int
    job_index: int
    doh_dol_job_index: int
    modifier_hit_points: int
    modifier_mana_points: int
    modifier_strength: int
    modifier_vitality: int
    modifier_dexterity: int
    modifier_intelligence: int
    modifier_mind: int
    modifier_piety: int
    pv_p_action_sort_row: int
    class_job_parent_id: Optional[int] = Field(default=None, foreign_key="class_job.id")
    class_job_parent: Optional["ClassJob"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[ClassJob.class_job_parent_id]"})
    name_english: str
    item_starting_weapon_id: Optional[int] = Field(default=None, foreign_key="item.id")
    item_starting_weapon: Optional["Item"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[ClassJob.item_starting_weapon_id]"})
    role: int
    starting_town_id: Optional[int] = Field(default=None, foreign_key="town.id")
    starting_town: Optional["Town"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[ClassJob.starting_town_id]"})
    monster_note_id: Optional[int] = Field(default=None, foreign_key="monster_note.id")
    monster_note: Optional["MonsterNote"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[ClassJob.monster_note_id]"})
    primary_stat: int
    limit_break1_id: Optional[int] = Field(default=None, foreign_key="action.id")
    limit_break1: Optional["Action"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[ClassJob.limit_break1_id]"})
    limit_break2_id: Optional[int] = Field(default=None, foreign_key="action.id")
    limit_break2: Optional["Action"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[ClassJob.limit_break2_id]"})
    limit_break3_id: Optional[int] = Field(default=None, foreign_key="action.id")
    limit_break3: Optional["Action"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[ClassJob.limit_break3_id]"})
    u_i_priority: int
    item_soul_crystal_id: Optional[int] = Field(default=None, foreign_key="item.id")
    item_soul_crystal: Optional["Item"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[ClassJob.item_soul_crystal_id]"})
    unlock_quest_id: Optional[int] = Field(default=None, foreign_key="quest.id")
    unlock_quest: Optional["Quest"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[ClassJob.unlock_quest_id]"})
    relic_quest_id: Optional[int] = Field(default=None, foreign_key="quest.id")
    relic_quest: Optional["Quest"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[ClassJob.relic_quest_id]"})
    prerequisite_id: Optional[int] = Field(default=None, foreign_key="quest.id")
    prerequisite: Optional["Quest"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[ClassJob.prerequisite_id]"})
    starting_level: int
    party_bonus: int
    is_limited_job: bool
    can_queue_for_duty: bool

