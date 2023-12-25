from sqlalchemy.orm import Mapped, mapped_column
from pydantic import BaseModel
from .. import TableBase


class AchievementTarget(TableBase):
    __tablename__ = "achievement_target"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    type: Mapped[int] = mapped_column()
    value: Mapped[int] = mapped_column()

    def to_schema(self):
        return AchievementTarget.Schema(
            id=self.id,
            type=self.type,
            value=self.value
        )

    class Schema(BaseModel):
        id: int
        type: int
        value: int
