from sqlalchemy.orm import Session
from fastapi import APIRouter

from ..storingway import engine
from ..storingway.models_generated.GatheringItem import GatheringItem
from ..storingway.models_generated.GatheringPointBase import GatheringPointBase
from ..storingway.models_generated.Item import Item


router = APIRouter(tags=["items"])


@router.get("/items/by_source/gathering/")
def items_bysource_gathering():
    with Session(engine) as session:
        data = session.query(GatheringPointBase).all()
        all_gathering_items: list[GatheringItem] = []
        for item in data:
            if (item.item0 is not None):
                all_gathering_items.append(item.item0)
            if (item.item1 is not None):
                all_gathering_items.append(item.item1)
            if (item.item2 is not None):
                all_gathering_items.append(item.item2)
            if (item.item3 is not None):
                all_gathering_items.append(item.item3)
            if (item.item4 is not None):
                all_gathering_items.append(item.item4)
            if (item.item5 is not None):
                all_gathering_items.append(item.item5)
            if (item.item6 is not None):
                all_gathering_items.append(item.item6)
            if (item.item7 is not None):
                all_gathering_items.append(item.item7)
        unique_gathering_items: list[GatheringItem] = []
        for gathering_item in all_gathering_items:
            if gathering_item not in unique_gathering_items and gathering_item is not None:
                unique_gathering_items.append(gathering_item)
        itemlist: list[Item] = [gi.item for gi in unique_gathering_items if gi.item is not None]
        itemnames = [f"{i.id}, {i.singular}" for i in itemlist]
        return itemnames
