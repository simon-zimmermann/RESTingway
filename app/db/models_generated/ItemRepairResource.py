from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from db.models_generated.Item import Item


class ItemRepairResource(SQLModel, table=True):
    __tablename__ = "item_repair_resource"
    __table_args__ = {'extend_existing': True}
    __allow_unmapped__ = True
    id: int = Field(default=None, primary_key=True)
    item_id: Optional[int] = Field(default=None, foreign_key="item.id")
    item: Optional["Item"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[ItemRepairResource.item_id]"})

