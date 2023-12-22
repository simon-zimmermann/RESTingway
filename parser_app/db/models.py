from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, SmallInteger
from sqlalchemy.orm import relationship
from pydantic import BaseModel
from . import Base


class AchievementKind(Base):
    __tablename__ = "AchievementKind"

    id = Column(Integer, primary_key=True, index=True)
    Name = Column(String)
    Order = Column(SmallInteger)

    def to_schema(self):
        return AchievementKind.Schema(
            id=self.id,
            Name=self.Name,
            Order=self.Order
        )

    class Schema(BaseModel):
        id: int
        Name: str
        Order: int


class AchievementCategory(Base):
    __tablename__ = "AchievementCategory"
    id = Column(Integer, primary_key=True, index=True)
    Name = Column(String)
    AchievementKind = Column(Integer, ForeignKey("AchievementKind.id"))
    ShowComplete = Column(Boolean)
    HideCategory = Column(Boolean)
    Order = Column(SmallInteger)

    def to_schema(self):
        return AchievementCategory.Schema(
            id=self.id,
            Name=self.Name,
            AchievementKind=self.AchievementKind,
            ShowComplete=self.ShowComplete,
            HideCategory=self.HideCategory,
            Order=self.Order
        )

    class Schema(BaseModel):
        id: int
        Name: str
        AchievementKind: int
        ShowComplete: bool
        HideCategory: bool
        Order: int
