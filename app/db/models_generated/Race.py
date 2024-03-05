from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from db.models_generated.Item import Item
    from db.models_generated.ExVersion import ExVersion


class Race(SQLModel, table=True):
    __tablename__ = "race"
    __table_args__ = {'extend_existing': True}
    __allow_unmapped__ = True
    id: int = Field(default=None, primary_key=True)
    masculine: str
    feminine: str
    r_s_e_m_body_id: Optional[int] = Field(default=None, foreign_key="item.id")
    r_s_e_m_body: Optional["Item"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Race.r_s_e_m_body_id]"})
    r_s_e_m_hands_id: Optional[int] = Field(default=None, foreign_key="item.id")
    r_s_e_m_hands: Optional["Item"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Race.r_s_e_m_hands_id]"})
    r_s_e_m_legs_id: Optional[int] = Field(default=None, foreign_key="item.id")
    r_s_e_m_legs: Optional["Item"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Race.r_s_e_m_legs_id]"})
    r_s_e_m_feet_id: Optional[int] = Field(default=None, foreign_key="item.id")
    r_s_e_m_feet: Optional["Item"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Race.r_s_e_m_feet_id]"})
    r_s_e_f_body_id: Optional[int] = Field(default=None, foreign_key="item.id")
    r_s_e_f_body: Optional["Item"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Race.r_s_e_f_body_id]"})
    r_s_e_f_hands_id: Optional[int] = Field(default=None, foreign_key="item.id")
    r_s_e_f_hands: Optional["Item"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Race.r_s_e_f_hands_id]"})
    r_s_e_f_legs_id: Optional[int] = Field(default=None, foreign_key="item.id")
    r_s_e_f_legs: Optional["Item"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Race.r_s_e_f_legs_id]"})
    r_s_e_f_feet_id: Optional[int] = Field(default=None, foreign_key="item.id")
    r_s_e_f_feet: Optional["Item"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Race.r_s_e_f_feet_id]"})
    ex_pac_id: Optional[int] = Field(default=None, foreign_key="ex_version.id")
    ex_pac: Optional["ExVersion"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Race.ex_pac_id]"})

