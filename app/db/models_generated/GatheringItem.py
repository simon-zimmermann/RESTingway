from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app.storingway.models_generated.Item import Item
    from app.storingway.models_generated.GatheringItemLevelConvertTable import GatheringItemLevelConvertTable
    from app.storingway.models_generated.Quest import Quest


class GatheringItem(SQLModel, table=True):
    __tablename__ = "gathering_item"
    __table_args__ = {'extend_existing': True}
    __allow_unmapped__ = True
    id: int = Field(default=None, primary_key=True)
    item_id: Optional[int] = Field(default=None, foreign_key="item.id")
    item: Optional["Item"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[GatheringItem.item_id]"})
    gathering_item_level_id: Optional[int] = Field(default=None, foreign_key="gathering_item_level_convert_table.id")
    gathering_item_level: Optional["GatheringItemLevelConvertTable"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[GatheringItem.gathering_item_level_id]"})
    quest_id: Optional[int] = Field(default=None, foreign_key="quest.id")
    quest: Optional["Quest"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[GatheringItem.quest_id]"})
    is_hidden: bool

