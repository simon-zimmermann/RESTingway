from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from db.models_generated.Item import Item


class BeastRankBonus(SQLModel, table=True):
    __tablename__ = "beast_rank_bonus"
    __table_args__ = {'extend_existing': True}
    __allow_unmapped__ = True
    id: int = Field(default=None, primary_key=True)
    neutral: int
    recognized: int
    friendly: int
    trusted: int
    respected: int
    honored: int
    sworn: int
    allied_bloodsworn: int
    item_id: Optional[int] = Field(default=None, foreign_key="item.id")
    item: Optional["Item"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[BeastRankBonus.item_id]"})
    item_quantity0: int
    item_quantity1: int
    item_quantity2: int
    item_quantity3: int
    item_quantity4: int
    item_quantity5: int
    item_quantity6: int
    item_quantity7: int

