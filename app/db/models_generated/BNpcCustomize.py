from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app.storingway.models_generated.Race import Race
    from app.storingway.models_generated.Tribe import Tribe


class BNpcCustomize(SQLModel, table=True):
    __tablename__ = "b_npc_customize"
    __table_args__ = {'extend_existing': True}
    __allow_unmapped__ = True
    id: int = Field(default=None, primary_key=True)
    race_id: Optional[int] = Field(default=None, foreign_key="race.id")
    race: Optional["Race"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[BNpcCustomize.race_id]"})
    gender: int
    body_type: int
    height: int
    tribe_id: Optional[int] = Field(default=None, foreign_key="tribe.id")
    tribe: Optional["Tribe"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[BNpcCustomize.tribe_id]"})
    face: int
    hair_style: int
    hair_highlight: int
    skin_color: int
    eye_heterochromia: int
    hair_color: int
    hair_highlight_color: int
    facial_feature: int
    facial_feature_color: int
    eyebrows: int
    eye_color: int
    eye_shape: int
    nose: int
    jaw: int
    mouth: int
    lip_color: int
    bust_or_tone1: int
    extra_feature1: int
    extra_feature2_or_bust: int
    face_paint: int
    face_paint_color: int

