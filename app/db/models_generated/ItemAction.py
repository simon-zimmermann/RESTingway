from typing import Optional
from sqlmodel import Field, SQLModel, Relationship


class ItemAction(SQLModel, table=True):
    __tablename__ = "item_action"
    __table_args__ = {'extend_existing': True}
    __allow_unmapped__ = True
    id: int = Field(default=None, primary_key=True)
    cond_lv: int
    cond_battle: bool
    cond_p_v_p: bool
    cond_p_v_p_only: bool
    type: int
    data0: int
    data1: int
    data2: int
    data3: int
    data4: int
    data5: int
    data6: int
    data7: int
    data8: int
    data_h_q0: int
    data_h_q1: int
    data_h_q2: int
    data_h_q3: int
    data_h_q4: int
    data_h_q5: int
    data_h_q6: int
    data_h_q7: int
    data_h_q8: int

