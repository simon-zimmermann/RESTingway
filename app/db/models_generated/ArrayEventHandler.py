from typing import Optional
from sqlmodel import Field, SQLModel, Relationship


class ArrayEventHandler(SQLModel, table=True):
    __tablename__ = "array_event_handler"
    __table_args__ = {'extend_existing': True}
    __allow_unmapped__ = True
    id: int = Field(default=None, primary_key=True)
    data0: int
    data1: int
    data2: int
    data3: int
    data4: int
    data5: int
    data6: int
    data7: int
    data8: int
    data9: int
    data10: int
    data11: int
    data12: int
    data13: int
    data14: int
    data15: int

