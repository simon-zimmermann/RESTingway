from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app.storingway.models_generated.AchievementKind import AchievementKind


class AchievementCategory(SQLModel, table=True):
    __tablename__ = "achievement_category"
    __table_args__ = {'extend_existing': True}
    __allow_unmapped__ = True
    id: int = Field(default=None, primary_key=True)
    name: str
    achievement_kind_id: Optional[int] = Field(default=None, foreign_key="achievement_kind.id")
    achievement_kind: Optional["AchievementKind"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[AchievementCategory.achievement_kind_id]"})
    show_complete: bool
    hide_category: bool
    order: int

