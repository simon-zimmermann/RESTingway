from fastapi import APIRouter


from .data_enums import GatheringTypes

from app.storingway.crud import crud_gathering

router = APIRouter(tags=["items"])


@router.get("/items/by_source/gathering/{type}")
def items_bysource_gathering(type: GatheringTypes):
    itemlist = crud_gathering.get_items_gatherable(type)
    itemnames = [f"{i.id}, {i.singular}" for i in itemlist]
    return itemnames
