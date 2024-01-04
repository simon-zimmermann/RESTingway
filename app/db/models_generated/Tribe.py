from typing import Optional
from sqlmodel import Field, SQLModel, Relationship


class Tribe(SQLModel, table=True):
    __tablename__ = "tribe"
    __table_args__ = {'extend_existing': True}
    __allow_unmapped__ = True
    id: int = Field(default=None, primary_key=True)
    masculine: str
    feminine: str
    hp: int
    mp: int
    s_t_r: int
    v_i_t: int
    d_e_x: int
    i_n_t: int
    m_n_d: int
    p_i_e: int

