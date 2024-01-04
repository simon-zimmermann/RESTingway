from typing import Optional
from sqlmodel import Field, SQLModel, Relationship


class BaseParam(SQLModel, table=True):
    __tablename__ = "base_param"
    __table_args__ = {'extend_existing': True}
    __allow_unmapped__ = True
    id: int = Field(default=None, primary_key=True)
    packet_index: int
    name: str
    description: str
    order_priority: int
    param_1_h_wpn: int
    o_h: int
    head: int
    chest: int
    hands: int
    waist: int
    legs: int
    feet: int
    earring: int
    necklace: int
    bracelet: int
    ring: int
    param_2_h_wpn: int
    under_armor: int
    chest_head: int
    chest_head_legs_feet: int
    legs_feet: int
    head_chest_hands_legs_feet: int
    chest_legs_gloves: int
    chest_legs_feet: int
    meld_param0: int
    meld_param1: int
    meld_param2: int
    meld_param3: int
    meld_param4: int
    meld_param5: int
    meld_param6: int
    meld_param7: int
    meld_param8: int
    meld_param9: int
    meld_param10: int
    meld_param11: int
    meld_param12: int

