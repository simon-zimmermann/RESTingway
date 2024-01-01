from sqlmodel import Session, select
from statistics import median

from app.storingway.models.UniversalisEntry import UniversalisEntry
from app.storingway import engine


def add_batch(data: list[UniversalisEntry]):
    with Session(engine) as session:
        for d in data:
            session.add(d)
        session.commit()


def remove_by_item(item_id: int):
    with Session(engine) as session:
        items = get_by_item(item_id)
        for item in items:
            session.delete(item)
        session.commit()


def get_by_item(item_id: int) -> list[UniversalisEntry]:
    with Session(engine) as session:
        statement = select(UniversalisEntry).filter(UniversalisEntry.item_id == item_id)
        return session.exec(statement).all()


def get_arithmethic_avg(item_id: int):
    data = get_by_item(item_id)
    listing_count = len(data)
    listing_sum = sum([entry.single_price for entry in data])
    arithmethic_avg = listing_sum / listing_count
    return arithmethic_avg


def get_median(item_id: int):
    data = get_by_item(item_id)
    return median([entry.single_price for entry in data])


def get_realistic_avg(item_id: int, buy_count: int = 99):
    data = get_by_item(item_id)
    # special average
    rolling_sum = 0
    rolling_count = 0
    current_weight = 1
    min_weight = 1 / 4
    buy_count_remaining = buy_count
    it = iter(data)
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
    return special_avg
