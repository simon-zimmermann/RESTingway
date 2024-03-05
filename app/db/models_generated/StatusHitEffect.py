from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from db.models_generated.VFX import VFX


class StatusHitEffect(SQLModel, table=True):
    __tablename__ = "status_hit_effect"
    __table_args__ = {'extend_existing': True}
    __allow_unmapped__ = True
    id: int = Field(default=None, primary_key=True)
    location_id: Optional[int] = Field(default=None, foreign_key="v_f_x.id")
    location: Optional["VFX"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[StatusHitEffect.location_id]"})

