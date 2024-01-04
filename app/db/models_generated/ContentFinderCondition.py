from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app.storingway.models_generated.TerritoryType import TerritoryType
    from app.storingway.models_generated.ClassJobCategory import ClassJobCategory
    from app.storingway.models_generated.ContentMemberType import ContentMemberType
    from app.storingway.models_generated.Quest import Quest
    from app.storingway.models_generated.ContentType import ContentType


class ContentFinderCondition(SQLModel, table=True):
    __tablename__ = "content_finder_condition"
    __table_args__ = {'extend_existing': True}
    __allow_unmapped__ = True
    id: int = Field(default=None, primary_key=True)
    short_code: str
    territory_type_id: Optional[int] = Field(default=None, foreign_key="territory_type.id")
    territory_type: Optional["TerritoryType"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[ContentFinderCondition.territory_type_id]"})
    content_link_type: int
    content: int
    pv_p: bool
    accept_class_job_category_id: Optional[int] = Field(default=None, foreign_key="class_job_category.id")
    accept_class_job_category: Optional["ClassJobCategory"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[ContentFinderCondition.accept_class_job_category_id]"})
    content_member_type_id: Optional[int] = Field(default=None, foreign_key="content_member_type.id")
    content_member_type: Optional["ContentMemberType"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[ContentFinderCondition.content_member_type_id]"})
    unlock_quest_id: Optional[int] = Field(default=None, foreign_key="quest.id")
    unlock_quest: Optional["Quest"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[ContentFinderCondition.unlock_quest_id]"})
    class_job_level_required: int
    class_job_level_sync: int
    item_level_required: int
    item_level_sync: int
    allow_undersized: bool
    allow_replacement: bool
    allow_explorer_mode: bool
    high_end_duty: bool
    duty_recorder_allowed: bool
    name: str
    name_short: str
    content_type_id: Optional[int] = Field(default=None, foreign_key="content_type.id")
    content_type: Optional["ContentType"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[ContentFinderCondition.content_type_id]"})
    transient_key: int
    transient: int
    sort_key: int
    image: str
    icon: str
    leveling_roulette: bool
    high_level_roulette: bool
    m_s_q_roulette: bool
    guild_hest_roulette: bool
    expert_roulette: bool
    trial_roulette: bool
    daily_frontline_challenge: bool
    level_cap_roulette: bool
    mentor_roulette: bool
    alliance_roulette: bool
    feast_team_roulette: bool
    normal_raid_roulette: bool

