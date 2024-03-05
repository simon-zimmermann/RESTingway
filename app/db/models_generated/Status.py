from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from db.models_generated.ClassJobCategory import ClassJobCategory
    from db.models_generated.StatusHitEffect import StatusHitEffect
    from db.models_generated.StatusLoopVFX import StatusLoopVFX


class Status(SQLModel, table=True):
    __tablename__ = "status"
    __table_args__ = {'extend_existing': True}
    __allow_unmapped__ = True
    id: int = Field(default=None, primary_key=True)
    name: str
    description: str
    icon: str
    max_stacks: int
    class_job_category_id: Optional[int] = Field(default=None, foreign_key="class_job_category.id")
    class_job_category: Optional["ClassJobCategory"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Status.class_job_category_id]"})
    status_category: int
    hit_effect_id: Optional[int] = Field(default=None, foreign_key="status_hit_effect.id")
    hit_effect: Optional["StatusHitEffect"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Status.hit_effect_id]"})
    v_f_x_id: Optional[int] = Field(default=None, foreign_key="status_loop_v_f_x.id")
    v_f_x: Optional["StatusLoopVFX"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Status.v_f_x_id]"})
    lock_movement: bool
    lock_actions: bool
    lock_control: bool
    transfiguration: bool
    is_gaze: bool
    can_dispel: bool
    inflicted_by_actor: bool
    is_permanent: bool
    party_list_priority: int
    can_increase_rewards: int
    param_modifier: int
    param_effect: int
    can_status_off: bool
    log: int
    is_fc_buff: bool
    invisibility: bool
    target_type: int
    flags: int

