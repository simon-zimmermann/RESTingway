from sqlalchemy.orm import Mapped, mapped_column
from pydantic import BaseModel
from .. import TableBase


class AchievementKind(TableBase):
    __tablename__ = "achievement_kind"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column()
    order: Mapped[int] = mapped_column()

    def __init__(self, csv_row, **kwargs):
        self.id = int(csv_row[0])
        self.name = csv_row[1]
        self.order = int(csv_row[2])
        super(AchievementKind, self).__init__(**kwargs)

    def to_schema(self):
        return AchievementKind.Schema(
            id=self.id,
            name=self.name,
            order=self.order
        )

    class Schema(BaseModel):
        id: int
        name: str
        order: int
