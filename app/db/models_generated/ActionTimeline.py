from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app.storingway.models_generated.WeaponTimeline import WeaponTimeline


class ActionTimeline(SQLModel, table=True):
    __tablename__ = "action_timeline"
    __table_args__ = {'extend_existing': True}
    __allow_unmapped__ = True
    id: int = Field(default=None, primary_key=True)
    type: int
    priority: int
    pause: bool
    stance: int
    slot: int
    look_at_mode: int
    key: str
    action_timeline_i_d_mode: int
    weapon_timeline_id: Optional[int] = Field(default=None, foreign_key="weapon_timeline.id")
    weapon_timeline: Optional["WeaponTimeline"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[ActionTimeline.weapon_timeline_id]"})
    load_type: int
    start_attach: int
    resident_pap: int
    resident: bool
    kill_upper: int
    is_motion_canceled_by_moving: bool
    is_loop: int

