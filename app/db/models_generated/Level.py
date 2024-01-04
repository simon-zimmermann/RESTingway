from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app.storingway.models_generated.Map import Map
    from app.storingway.models_generated.TerritoryType import TerritoryType


class Level(SQLModel, table=True):
    __tablename__ = "level"
    __table_args__ = {'extend_existing': True}
    __allow_unmapped__ = True
    id: int = Field(default=None, primary_key=True)
    x: float
    y: float
    z: float
    yaw: float
    radius: float
    type: int
    object: int
    map_id: Optional[int] = Field(default=None, foreign_key="map.id")
    map: Optional["Map"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Level.map_id]"})
    event_id: int
    territory_id: Optional[int] = Field(default=None, foreign_key="territory_type.id")
    territory: Optional["TerritoryType"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Level.territory_id]"})

