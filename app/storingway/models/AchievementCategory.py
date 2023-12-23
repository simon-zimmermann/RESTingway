from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from pydantic import BaseModel

from .AchievementKind import AchievementKind
from .. import TableBase


class AchievementCategory(TableBase):  # parent
    __tablename__ = "achievement_category"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column()
    achievement_kind_id: Mapped[int] = mapped_column(ForeignKey("achievement_kind.id"))
    achievement_kind: Mapped[AchievementKind] = relationship("AchievementKind")
    show_complete: Mapped[bool] = mapped_column()
    hide_category: Mapped[bool] = mapped_column()
    order: Mapped[int] = mapped_column()

    def __init__(self, csv_row, **kwargs):
        self.id = int(csv_row[0])
        self.name = csv_row[1]
        self.achievement_kind_id = int(csv_row[2])
        self.show_complete = bool(csv_row[3])
        self.hide_category = bool(csv_row[4])
        self.order = int(csv_row[5])
        super(AchievementCategory, self).__init__(**kwargs)

    def to_schema(self):
        return AchievementCategory.Schema(
            id=self.id,
            name=self.name,
            achievementKind=self.achievement_kind.to_schema(),
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
