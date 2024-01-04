from typing import Optional
from sqlmodel import Field, SQLModel, Relationship


class EquipSlotCategory(SQLModel, table=True):
    __tablename__ = "equip_slot_category"
    __table_args__ = {'extend_existing': True}
    __allow_unmapped__ = True
    id: int = Field(default=None, primary_key=True)
    main_hand: int
    off_hand: int
    head: int
    body: int
    gloves: int
    waist: int
    legs: int
    feet: int
    ears: int
    neck: int
    wrists: int
    finger_l: int
    finger_r: int
    soul_crystal: int

