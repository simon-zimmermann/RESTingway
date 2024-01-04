from typing import Optional
from sqlmodel import Field, SQLModel, Relationship


class ItemUICategory(SQLModel, table=True):
    __tablename__ = "item_u_i_category"
    __table_args__ = {'extend_existing': True}
    __allow_unmapped__ = True
    id: int = Field(default=None, primary_key=True)
    name: str
    icon: str
    order_minor: int
    order_major: int

