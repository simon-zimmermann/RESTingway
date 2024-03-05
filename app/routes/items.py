from fastapi import APIRouter


from app.db.crud import gathering

router = APIRouter(tags=["items"])


@router.get("/items/by_source/gathering/{type}")
def items_bysource_gathering(type: gathering.GatheringTypes) -> list[str]:
    itemlist = gathering.get_gatherable_by(type)
    itemnames = [f"{i.id}, {i.singular}" for i in itemlist]
    return itemnames
