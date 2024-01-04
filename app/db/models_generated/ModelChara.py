from typing import Optional
from sqlmodel import Field, SQLModel, Relationship


class ModelChara(SQLModel, table=True):
    __tablename__ = "model_chara"
    __table_args__ = {'extend_existing': True}
    __allow_unmapped__ = True
    id: int = Field(default=None, primary_key=True)
    type: int
    model: int
    base: int
    variant: int
    s_e_pack: int
    pap_variation: bool

