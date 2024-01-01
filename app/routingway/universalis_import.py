from fastapi import APIRouter, BackgroundTasks
import requests
from datetime import datetime
from statistics import median

from app.storingway.crud import crud_universalis
from app.storingway.crud import crud_gathering
from app.storingway.models.UniversalisEntry import UniversalisEntry
from app.routingway.responses import BasicResponse
from app.connectingway.universalis_cycle import refresh_universalis_data


router = APIRouter(tags=["universalis"])


@router.patch("/universalis/start_cycle")
def universalis_start_cycle(background_tasks: BackgroundTasks):
    background_tasks.add_task(refresh_universalis_data)
    return BasicResponse(status="Universalis refresh cycle started.")


@router.patch("/universalis_import/full")
def universalis_import_full():
    importlist = crud_gathering.get_items_gatherable(1, 20)
    for item in importlist:
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


@router.get("/universalis_import/realistic_avg")
def universalis_import_realistic_avg(item_id: int, buy_count: int = 99):
    listings = crud_universalis.get_by_item(item_id)
    listings.sort(key=lambda x: x.single_price)
    # arithmethic average
    listing_count = len(listings)
    listing_sum = sum([listing.single_price for listing in listings])
    arithmethic_avg = listing_sum / listing_count
    print(f"arithmethic_avg: {arithmethic_avg}")
    # median average
    median_avg = median([listing.single_price for listing in listings])
    print(f"median_avg: {median_avg}")
    # special average
    rolling_sum = 0
    rolling_count = 0
    current_weight = 1
    min_weight = 1 / 4
    buy_count_remaining = buy_count
    it = iter(listings)
    try:
        curr_price = 0
        curr_count = 0
        while True:
            # weight has been reduced low enough -> calculation is complete
            if current_weight < min_weight:
                break
            # current listing is exhausted -> get next listing
            elif curr_count == 0:
                curr_listing = next(it)
                curr_price = curr_listing.single_price
                curr_count = curr_listing.quantity
            # current weight is exhausted -> reduce weight and reset buy_count_remaining
            elif buy_count_remaining == 0:
                buy_count_remaining = buy_count
                current_weight /= 2
            # we can buy all items from this listing -> do so
            elif buy_count_remaining >= curr_count:
                buy_count_remaining -= curr_count
                rolling_sum += curr_price * curr_count * current_weight
                rolling_count += curr_count * current_weight
                curr_count = 0
            # we cant buy all items from this listing with the current weight -> buy as many as we can
            else:
                curr_count -= buy_count_remaining
                rolling_sum += curr_price * buy_count_remaining * current_weight
                rolling_count += buy_count_remaining * current_weight
                buy_count_remaining = 0

    except StopIteration:
        pass

    special_avg = rolling_sum / rolling_count
    print(f"special_avg: {special_avg}")
