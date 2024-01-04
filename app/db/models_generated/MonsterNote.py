from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app.storingway.models_generated.MonsterNoteTarget import MonsterNoteTarget


class MonsterNote(SQLModel, table=True):
    __tablename__ = "monster_note"
    __table_args__ = {'extend_existing': True}
    __allow_unmapped__ = True
    id: int = Field(default=None, primary_key=True)
    monster_note_target0_id: Optional[int] = Field(default=None, foreign_key="monster_note_target.id")
    monster_note_target0: Optional["MonsterNoteTarget"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[MonsterNote.monster_note_target0_id]"})
    monster_note_target1_id: Optional[int] = Field(default=None, foreign_key="monster_note_target.id")
    monster_note_target1: Optional["MonsterNoteTarget"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[MonsterNote.monster_note_target1_id]"})
    monster_note_target2_id: Optional[int] = Field(default=None, foreign_key="monster_note_target.id")
    monster_note_target2: Optional["MonsterNoteTarget"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[MonsterNote.monster_note_target2_id]"})
    monster_note_target3_id: Optional[int] = Field(default=None, foreign_key="monster_note_target.id")
    monster_note_target3: Optional["MonsterNoteTarget"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[MonsterNote.monster_note_target3_id]"})
    count0: int
    count1: int
    count2: int
    count3: int
    reward: int
    name: str

