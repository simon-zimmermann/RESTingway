from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app.storingway.models_generated.ClassJob import ClassJob


class ItemSearchCategory(SQLModel, table=True):
    __tablename__ = "item_search_category"
    __table_args__ = {'extend_existing': True}
    __allow_unmapped__ = True
    id: int = Field(default=None, primary_key=True)
    name: str
    icon: str
    category: int
    order: int
    class_job_id: Optional[int] = Field(default=None, foreign_key="class_job.id")
    class_job: Optional["ClassJob"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[ItemSearchCategory.class_job_id]"})

