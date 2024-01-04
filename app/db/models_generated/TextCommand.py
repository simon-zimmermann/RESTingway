from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app.storingway.models_generated.TextCommandParam import TextCommandParam


class TextCommand(SQLModel, table=True):
    __tablename__ = "text_command"
    __table_args__ = {'extend_existing': True}
    __allow_unmapped__ = True
    id: int = Field(default=None, primary_key=True)
    command: str
    short_command: str
    description: str
    alias: str
    short_alias: str
    param_id: Optional[int] = Field(default=None, foreign_key="text_command_param.id")
    param: Optional["TextCommandParam"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[TextCommand.param_id]"})

