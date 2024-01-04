from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app.storingway.models_generated.AchievementCategory import AchievementCategory
    from app.storingway.models_generated.AchievementTarget import AchievementTarget
    from app.storingway.models_generated.Title import Title
    from app.storingway.models_generated.Item import Item
    from app.storingway.models_generated.AchievementHideCondition import AchievementHideCondition


class Achievement(SQLModel, table=True):
    __tablename__ = "achievement"
    __table_args__ = {'extend_existing': True}
    __allow_unmapped__ = True
    id: int = Field(default=None, primary_key=True)
    achievement_category_id: Optional[int] = Field(default=None, foreign_key="achievement_category.id")
    achievement_category: Optional["AchievementCategory"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Achievement.achievement_category_id]"})
    name: str
    description: str
    achievement_target_id: Optional[int] = Field(default=None, foreign_key="achievement_target.id")
    achievement_target: Optional["AchievementTarget"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Achievement.achievement_target_id]"})
    points: int
    title_id: Optional[int] = Field(default=None, foreign_key="title.id")
    title: Optional["Title"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Achievement.title_id]"})
    item_id: Optional[int] = Field(default=None, foreign_key="item.id")
    item: Optional["Item"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Achievement.item_id]"})
    icon: str
    type: int
    key: int
    data0: int
    data1: int
    data2: int
    data3: int
    data4: int
    data5: int
    data6: int
    data7: int
    order: int
    achievement_hide_condition_id: Optional[int] = Field(default=None, foreign_key="achievement_hide_condition.id")
    achievement_hide_condition: Optional["AchievementHideCondition"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Achievement.achievement_hide_condition_id]"})

