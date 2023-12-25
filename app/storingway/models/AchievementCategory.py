from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from pydantic import BaseModel

from .AchievementKind import AchievementKind
from .. import TableBase


class AchievementCategory(TableBase):
    __tablename__ = "achievement_category"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column()
    achievement_kinda: Mapped[int] = mapped_column(ForeignKey("achievement_kind.id"))
    achievement_kind_obj: Mapped[AchievementKind] = relationship("AchievementKind")
    show_complete: Mapped[bool] = mapped_column()
    hide_category: Mapped[bool] = mapped_column()
    order: Mapped[int] = mapped_column()

    def to_schema(self):
        return AchievementCategory.Schema(
            id=self.id,
            name=self.name,
            achievementKind=self.achievement_kind_obj.to_schema(),
            showComplete=self.show_complete,
            hideCategory=self.hide_category,
            order=self.order
        )

    class Schema(BaseModel):
        id: int
        name: str
        achievementKind: AchievementKind.Schema
        showComplete: bool
        hideCategory: bool
        order: int
