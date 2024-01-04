from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app.storingway.models_generated.Jingle import Jingle


class ScreenImage(SQLModel, table=True):
    __tablename__ = "screen_image"
    __table_args__ = {'extend_existing': True}
    __allow_unmapped__ = True
    id: int = Field(default=None, primary_key=True)
    image: str
    jingle_id: Optional[int] = Field(default=None, foreign_key="jingle.id")
    jingle: Optional["Jingle"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[ScreenImage.jingle_id]"})
    type: int
    lang: bool

