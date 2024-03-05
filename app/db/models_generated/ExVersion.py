from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from db.models_generated.ScreenImage import ScreenImage


class ExVersion(SQLModel, table=True):
    __tablename__ = "ex_version"
    __table_args__ = {'extend_existing': True}
    __allow_unmapped__ = True
    id: int = Field(default=None, primary_key=True)
    name: str
    accept_jingle_id: Optional[int] = Field(default=None, foreign_key="screen_image.id")
    accept_jingle: Optional["ScreenImage"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[ExVersion.accept_jingle_id]"})
    complete_jingle_id: Optional[int] = Field(default=None, foreign_key="screen_image.id")
    complete_jingle: Optional["ScreenImage"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[ExVersion.complete_jingle_id]"})

