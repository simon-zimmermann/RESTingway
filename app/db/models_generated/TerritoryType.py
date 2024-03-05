from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from db.models_generated.PlaceName import PlaceName
    from db.models_generated.Map import Map
    from db.models_generated.LoadingImage import LoadingImage
    from db.models_generated.ContentFinderCondition import ContentFinderCondition
    from db.models_generated.ArrayEventHandler import ArrayEventHandler
    from db.models_generated.QuestBattle import QuestBattle
    from db.models_generated.Aetheryte import Aetheryte
    from db.models_generated.ExVersion import ExVersion
    from db.models_generated.MountSpeed import MountSpeed


class TerritoryType(SQLModel, table=True):
    __tablename__ = "territory_type"
    __table_args__ = {'extend_existing': True}
    __allow_unmapped__ = True
    id: int = Field(default=None, primary_key=True)
    name: str
    bg: str
    battalion_mode: int
    place_name_region_id: Optional[int] = Field(default=None, foreign_key="place_name.id")
    place_name_region: Optional["PlaceName"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[TerritoryType.place_name_region_id]"})
    place_name_zone_id: Optional[int] = Field(default=None, foreign_key="place_name.id")
    place_name_zone: Optional["PlaceName"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[TerritoryType.place_name_zone_id]"})
    place_name_id: Optional[int] = Field(default=None, foreign_key="place_name.id")
    place_name: Optional["PlaceName"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[TerritoryType.place_name_id]"})
    map_id: Optional[int] = Field(default=None, foreign_key="map.id")
    map: Optional["Map"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[TerritoryType.map_id]"})
    loading_image_id: Optional[int] = Field(default=None, foreign_key="loading_image.id")
    loading_image: Optional["LoadingImage"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[TerritoryType.loading_image_id]"})
    exclusive_type: int
    territory_intended_use: int
    content_finder_condition_id: Optional[int] = Field(default=None, foreign_key="content_finder_condition.id")
    content_finder_condition: Optional["ContentFinderCondition"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[TerritoryType.content_finder_condition_id]"})
    weather_rate: int
    p_c_search: bool
    stealth: bool
    mount: bool
    b_g_m: int
    place_name_region_icon: str
    place_name_icon: str
    array_event_handler_id: Optional[int] = Field(default=None, foreign_key="array_event_handler.id")
    array_event_handler: Optional["ArrayEventHandler"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[TerritoryType.array_event_handler_id]"})
    quest_battle_id: Optional[int] = Field(default=None, foreign_key="quest_battle.id")
    quest_battle: Optional["QuestBattle"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[TerritoryType.quest_battle_id]"})
    aetheryte_id: Optional[int] = Field(default=None, foreign_key="aetheryte.id")
    aetheryte: Optional["Aetheryte"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[TerritoryType.aetheryte_id]"})
    fixed_time: int
    resident: int
    achievement_index: int
    is_pvp_zone: bool
    ex_version_id: Optional[int] = Field(default=None, foreign_key="ex_version.id")
    ex_version: Optional["ExVersion"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[TerritoryType.ex_version_id]"})
    mount_speed_id: Optional[int] = Field(default=None, foreign_key="mount_speed.id")
    mount_speed: Optional["MountSpeed"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[TerritoryType.mount_speed_id]"})

