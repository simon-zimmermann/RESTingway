from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app.storingway.models_generated.GatheringType import GatheringType
    from app.storingway.models_generated.GatheringItem import GatheringItem


class GatheringPointBase(SQLModel, table=True):
    __tablename__ = "gathering_point_base"
    __table_args__ = {'extend_existing': True}
    __allow_unmapped__ = True
    id: int = Field(default=None, primary_key=True)
    gathering_type_id: Optional[int] = Field(default=None, foreign_key="gathering_type.id")
    gathering_type: Optional["GatheringType"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[GatheringPointBase.gathering_type_id]"})
    gathering_level: int
    item0_id: Optional[int] = Field(default=None, foreign_key="gathering_item.id")
    item0: Optional["GatheringItem"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[GatheringPointBase.item0_id]"})
    item1_id: Optional[int] = Field(default=None, foreign_key="gathering_item.id")
    item1: Optional["GatheringItem"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[GatheringPointBase.item1_id]"})
    item2_id: Optional[int] = Field(default=None, foreign_key="gathering_item.id")
    item2: Optional["GatheringItem"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[GatheringPointBase.item2_id]"})
    item3_id: Optional[int] = Field(default=None, foreign_key="gathering_item.id")
    item3: Optional["GatheringItem"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[GatheringPointBase.item3_id]"})
    item4_id: Optional[int] = Field(default=None, foreign_key="gathering_item.id")
    item4: Optional["GatheringItem"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[GatheringPointBase.item4_id]"})
    item5_id: Optional[int] = Field(default=None, foreign_key="gathering_item.id")
    item5: Optional["GatheringItem"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[GatheringPointBase.item5_id]"})
    item6_id: Optional[int] = Field(default=None, foreign_key="gathering_item.id")
    item6: Optional["GatheringItem"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[GatheringPointBase.item6_id]"})
    item7_id: Optional[int] = Field(default=None, foreign_key="gathering_item.id")
    item7: Optional["GatheringItem"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[GatheringPointBase.item7_id]"})

