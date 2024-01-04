from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from db.models_generated.ClassJobCategory import ClassJobCategory
    from db.models_generated.ENpcResident import ENpcResident
    from db.models_generated.Item import Item


class QuestClassJobSupply(SQLModel, table=True):
    __tablename__ = "quest_class_job_supply"
    __table_args__ = {'extend_existing': True}
    __allow_unmapped__ = True
    id: int = Field(default=None, primary_key=True)
    class_job_category_id: Optional[int] = Field(default=None, foreign_key="class_job_category.id")
    class_job_category: Optional["ClassJobCategory"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[QuestClassJobSupply.class_job_category_id]"})
    e_npc_resident_id: Optional[int] = Field(default=None, foreign_key="e_npc_resident.id")
    e_npc_resident: Optional["ENpcResident"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[QuestClassJobSupply.e_npc_resident_id]"})
    item_id: Optional[int] = Field(default=None, foreign_key="item.id")
    item: Optional["Item"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[QuestClassJobSupply.item_id]"})
    amount_required: int
    item_h_q: bool

