from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from db.models_generated.ActionCategory import ActionCategory
    from db.models_generated.ActionCastTimeline import ActionCastTimeline
    from db.models_generated.ActionCastVFX import ActionCastVFX
    from db.models_generated.ActionTimeline import ActionTimeline
    from db.models_generated.ClassJob import ClassJob
    from db.models_generated.AttackType import AttackType
    from db.models_generated.ActionProcStatus import ActionProcStatus
    from db.models_generated.Status import Status
    from db.models_generated.ClassJobCategory import ClassJobCategory
    from db.models_generated.Omen import Omen


class Action(SQLModel, table=True):
    __tablename__ = "action"
    __table_args__ = {'extend_existing': True}
    __allow_unmapped__ = True
    id: int = Field(default=None, primary_key=True)
    name: str
    icon: str
    action_category_id: Optional[int] = Field(default=None, foreign_key="action_category.id")
    action_category: Optional["ActionCategory"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Action.action_category_id]"})
    animation_start_id: Optional[int] = Field(default=None, foreign_key="action_cast_timeline.id")
    animation_start: Optional["ActionCastTimeline"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Action.animation_start_id]"})
    v_f_x_id: Optional[int] = Field(default=None, foreign_key="action_cast_v_f_x.id")
    v_f_x: Optional["ActionCastVFX"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Action.v_f_x_id]"})
    animation_end_id: Optional[int] = Field(default=None, foreign_key="action_timeline.id")
    animation_end: Optional["ActionTimeline"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Action.animation_end_id]"})
    action_timeline_hit_id: Optional[int] = Field(default=None, foreign_key="action_timeline.id")
    action_timeline_hit: Optional["ActionTimeline"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Action.action_timeline_hit_id]"})
    class_job_id: Optional[int] = Field(default=None, foreign_key="class_job.id")
    class_job: Optional["ClassJob"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Action.class_job_id]"})
    behaviour_type: int
    class_job_level: int
    is_role_action: bool
    range: int
    can_target_self: bool
    can_target_party: bool
    can_target_friendly: bool
    can_target_hostile: bool
    target_area: bool
    can_target_dead: bool
    cast_type: int
    effect_range: int
    x_axis_modifier: int
    primary_cost_type: int
    primary_cost_value: int
    secondary_cost_type: int
    secondary_cost_value: int
    action_combo_id: Optional[int] = Field(default=None, foreign_key="action.id")
    action_combo: Optional["Action"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Action.action_combo_id]"})
    preserves_combo: bool
    cast100ms: int
    recast100ms: int
    cooldown_group: int
    additional_cooldown_group: int
    max_charges: int
    attack_type_id: Optional[int] = Field(default=None, foreign_key="attack_type.id")
    attack_type: Optional["AttackType"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Action.attack_type_id]"})
    aspect: int
    action_proc_status_id: Optional[int] = Field(default=None, foreign_key="action_proc_status.id")
    action_proc_status: Optional["ActionProcStatus"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Action.action_proc_status_id]"})
    status_gain_self_id: Optional[int] = Field(default=None, foreign_key="status.id")
    status_gain_self: Optional["Status"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Action.status_gain_self_id]"})
    unlock_link: int
    class_job_category_id: Optional[int] = Field(default=None, foreign_key="class_job_category.id")
    class_job_category: Optional["ClassJobCategory"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Action.class_job_category_id]"})
    affects_position: bool
    omen_id: Optional[int] = Field(default=None, foreign_key="omen.id")
    omen: Optional["Omen"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Action.omen_id]"})
    is_pv_p: bool
    is_player_action: bool

