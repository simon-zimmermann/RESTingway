from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app.storingway.models_generated.Emote import Emote


class EmoteMode(SQLModel, table=True):
    __tablename__ = "emote_mode"
    __table_args__ = {'extend_existing': True}
    __allow_unmapped__ = True
    id: int = Field(default=None, primary_key=True)
    start_emote_id: Optional[int] = Field(default=None, foreign_key="emote.id")
    start_emote: Optional["Emote"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[EmoteMode.start_emote_id]"})
    end_emote_id: Optional[int] = Field(default=None, foreign_key="emote.id")
    end_emote: Optional["Emote"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[EmoteMode.end_emote_id]"})
    move: bool
    camera: bool
    end_on_rotate: bool
    end_on_emote: bool
    condition_mode: int

