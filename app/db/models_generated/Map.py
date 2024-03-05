from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from db.models_generated.MapCondition import MapCondition
    from db.models_generated.PlaceName import PlaceName
    from db.models_generated.TerritoryType import TerritoryType


class Map(SQLModel, table=True):
    __tablename__ = "map"
    __table_args__ = {'extend_existing': True}
    __allow_unmapped__ = True
    id: int = Field(default=None, primary_key=True)
    map_condition_id: Optional[int] = Field(default=None, foreign_key="map_condition.id")
    map_condition: Optional["MapCondition"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Map.map_condition_id]"})
    priority_category_u_i: int
    priority_u_i: int
    map_index: int
    hierarchy: int
    map_marker_range: int
    param_id: str
    size_factor: int
    offset_x: int
    offset_y: int
    place_name_region_id: Optional[int] = Field(default=None, foreign_key="place_name.id")
    place_name_region: Optional["PlaceName"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Map.place_name_region_id]"})
    place_name_id: Optional[int] = Field(default=None, foreign_key="place_name.id")
    place_name: Optional["PlaceName"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Map.place_name_id]"})
    place_name_sub_id: Optional[int] = Field(default=None, foreign_key="place_name.id")
    place_name_sub: Optional["PlaceName"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Map.place_name_sub_id]"})
    discovery_index: int
    discovery_flag: int
    territory_type_id: Optional[int] = Field(default=None, foreign_key="territory_type.id")
    territory_type: Optional["TerritoryType"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Map.territory_type_id]"})
    discovery_array_byte: bool
    is_event: bool

