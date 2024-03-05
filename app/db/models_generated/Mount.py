from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from db.models_generated.ModelChara import ModelChara
    from db.models_generated.MountFlyingCondition import MountFlyingCondition
    from db.models_generated.MountCustomize import MountCustomize
    from db.models_generated.BGM import BGM
    from db.models_generated.MountAction import MountAction


class Mount(SQLModel, table=True):
    __tablename__ = "mount"
    __table_args__ = {'extend_existing': True}
    __allow_unmapped__ = True
    id: int = Field(default=None, primary_key=True)
    singular: str
    adjective: int
    plural: str
    possessive_pronoun: int
    starts_with_vowel: int
    pronoun: int
    article: int
    model_chara_id: Optional[int] = Field(default=None, foreign_key="model_chara.id")
    model_chara: Optional["ModelChara"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Mount.model_chara_id]"})
    flying_condition_id: Optional[int] = Field(default=None, foreign_key="mount_flying_condition.id")
    flying_condition: Optional["MountFlyingCondition"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Mount.flying_condition_id]"})
    is_flying: int
    mount_customize_id: Optional[int] = Field(default=None, foreign_key="mount_customize.id")
    mount_customize: Optional["MountCustomize"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Mount.mount_customize_id]"})
    ride_b_g_m_id: Optional[int] = Field(default=None, foreign_key="b_g_m.id")
    ride_b_g_m: Optional["BGM"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Mount.ride_b_g_m_id]"})
    exit_move_dist: int
    exit_move_speed: int
    is_emote: bool
    equip_head: int
    equip_body: int
    equip_leg: int
    equip_foot: int
    order: int
    icon: str
    u_i_priority: int
    radius_rate: int
    base_motion_speed__run: int
    base_motion_speed__walk: int
    extra_seats: int
    mount_action_id: Optional[int] = Field(default=None, foreign_key="mount_action.id")
    mount_action: Optional["MountAction"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Mount.mount_action_id]"})
    is_airborne: bool
    ex_hotbar_enable_config: bool
    use_e_p: bool
    is_immobile: bool

