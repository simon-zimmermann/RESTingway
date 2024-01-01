import requests
from datetime import datetime

from app.storingway.crud import crud_gathering
from app.routingway.data_enums import GatheringTypes
from app.storingway.models_generated.Item import Item
from app.storingway.crud import crud_universalis
from app.storingway.models.UniversalisEntry import UniversalisEntry


def request_single_item(item: Item):
    # remove old entries for this item
    crud_universalis.remove_by_item(item.id)
    # get new entries for this item
    url = f"https://universalis.app/api/v2/light/{item.id}?fields=itemID%2Clistings"
    r = requests.get(url).json()
    # add all current listings on the marketboard
    db_obj_batch: list[UniversalisEntry] = []
    for listing in r["listings"]:
        keydict = {
            "item_id": int(r["itemID"]),
            "quantity": int(listing["quantity"]),
            "hq": bool(listing["hq"]),
            "last_review_time": datetime.fromtimestamp(int(listing["lastReviewTime"])),
            "last_import_time": datetime.now(),
            "single_price": int(listing["pricePerUnit"]),
            "world_id": int(listing["worldID"]),
        }
        db_obj = UniversalisEntry(**keydict)
        db_obj_batch.append(db_obj)
    crud_universalis.add_batch(db_obj_batch)


def refresh_universalis_data():
    debug_limit = 10
    itemlist: list[Item] = []
    for method in GatheringTypes:
        itemlist += crud_gathering.get_items_gatherable(method, debug_limit)
    print(f"requesting univeralis items: {[item.name for item in itemlist]}")
    print(f"count: {len(itemlist)}")
    for item in itemlist:  # TODO rate limit
        print(f"requesting data for {item.name} from universalis")
        request_single_item(item)

    realistic_avg_list: list[tuple[Item, float]] = []
    for item in itemlist:
        realistic_avg = crud_universalis.get_realistic_avg(item.id)
        realistic_avg_list.append((item, realistic_avg))
    # realistic_avg_list.sort(key=lambda x: x[1])

    print("realistic_avg_list: ")
    for item, avg in realistic_avg_list:
        print(f"{item.name}: {avg}")
