from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app.storingway.models_generated.BeastRankBonus import BeastRankBonus
    from app.storingway.models_generated.ExVersion import ExVersion
    from app.storingway.models_generated.Item import Item


class BeastTribe(SQLModel, table=True):
    __tablename__ = "beast_tribe"
    __table_args__ = {'extend_existing': True}
    __allow_unmapped__ = True
    id: int = Field(default=None, primary_key=True)
    min_level: int
    beast_rank_bonus_id: Optional[int] = Field(default=None, foreign_key="beast_rank_bonus.id")
    beast_rank_bonus: Optional["BeastRankBonus"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[BeastTribe.beast_rank_bonus_id]"})
    icon_reputation: str
    icon: str
    max_rank: int
    expansion_id: Optional[int] = Field(default=None, foreign_key="ex_version.id")
    expansion: Optional["ExVersion"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[BeastTribe.expansion_id]"})
    currency_item_id: Optional[int] = Field(default=None, foreign_key="item.id")
    currency_item: Optional["Item"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[BeastTribe.currency_item_id]"})
    display_order: int
    name: str
    adjective: int
    plural: str
    possessive_pronoun: int
    starts_with_vowel: int
    pronoun: int
    article: int
    d_e_f: int
    name_relation: str

