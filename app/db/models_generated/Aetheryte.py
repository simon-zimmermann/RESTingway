from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from db.models_generated.PlaceName import PlaceName
    from db.models_generated.TerritoryType import TerritoryType
    from db.models_generated.Level import Level
    from db.models_generated.Quest import Quest
    from db.models_generated.Map import Map


class Aetheryte(SQLModel, table=True):
    __tablename__ = "aetheryte"
    __table_args__ = {'extend_existing': True}
    __allow_unmapped__ = True
    id: int = Field(default=None, primary_key=True)
    singular: str
    adjective: int
    plural: str
    possessive_pronoun: int
    starts_with_vowel: int
    pronoun: int
    article: int
    place_name_id: Optional[int] = Field(default=None, foreign_key="place_name.id")
    place_name: Optional["PlaceName"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Aetheryte.place_name_id]"})
    aethernet_name_id: Optional[int] = Field(default=None, foreign_key="place_name.id")
    aethernet_name: Optional["PlaceName"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Aetheryte.aethernet_name_id]"})
    territory_id: Optional[int] = Field(default=None, foreign_key="territory_type.id")
    territory: Optional["TerritoryType"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Aetheryte.territory_id]"})
    level0_id: Optional[int] = Field(default=None, foreign_key="level.id")
    level0: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Aetheryte.level0_id]"})
    level1_id: Optional[int] = Field(default=None, foreign_key="level.id")
    level1: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Aetheryte.level1_id]"})
    level2_id: Optional[int] = Field(default=None, foreign_key="level.id")
    level2: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Aetheryte.level2_id]"})
    level3_id: Optional[int] = Field(default=None, foreign_key="level.id")
    level3: Optional["Level"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Aetheryte.level3_id]"})
    is_aetheryte: bool
    aethernet_group: int
    invisible: bool
    required_quest_id: Optional[int] = Field(default=None, foreign_key="quest.id")
    required_quest: Optional["Quest"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Aetheryte.required_quest_id]"})
    map_id: Optional[int] = Field(default=None, foreign_key="map.id")
    map: Optional["Map"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Aetheryte.map_id]"})
    aetherstream_x: int
    aetherstream_y: int
    order: int

