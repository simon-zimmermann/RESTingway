from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from db.models_generated.BNpcName import BNpcName
    from db.models_generated.Town import Town
    from db.models_generated.PlaceName import PlaceName


class MonsterNoteTarget(SQLModel, table=True):
    __tablename__ = "monster_note_target"
    __table_args__ = {'extend_existing': True}
    __allow_unmapped__ = True
    id: int = Field(default=None, primary_key=True)
    b_npc_name_id: Optional[int] = Field(default=None, foreign_key="b_npc_name.id")
    b_npc_name: Optional["BNpcName"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[MonsterNoteTarget.b_npc_name_id]"})
    icon: str
    town_id: Optional[int] = Field(default=None, foreign_key="town.id")
    town: Optional["Town"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[MonsterNoteTarget.town_id]"})
    place_name_zone0_id: Optional[int] = Field(default=None, foreign_key="place_name.id")
    place_name_zone0: Optional["PlaceName"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[MonsterNoteTarget.place_name_zone0_id]"})
    place_name_location0_id: Optional[int] = Field(default=None, foreign_key="place_name.id")
    place_name_location0: Optional["PlaceName"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[MonsterNoteTarget.place_name_location0_id]"})
    place_name_zone1_id: Optional[int] = Field(default=None, foreign_key="place_name.id")
    place_name_zone1: Optional["PlaceName"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[MonsterNoteTarget.place_name_zone1_id]"})
    place_name_location1_id: Optional[int] = Field(default=None, foreign_key="place_name.id")
    place_name_location1: Optional["PlaceName"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[MonsterNoteTarget.place_name_location1_id]"})
    place_name_zone2_id: Optional[int] = Field(default=None, foreign_key="place_name.id")
    place_name_zone2: Optional["PlaceName"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[MonsterNoteTarget.place_name_zone2_id]"})
    place_name_location2_id: Optional[int] = Field(default=None, foreign_key="place_name.id")
    place_name_location2: Optional["PlaceName"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[MonsterNoteTarget.place_name_location2_id]"})

