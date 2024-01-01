from sqlalchemy.orm import Session

from app.storingway.models.UniversalisEntry import UniversalisEntry
from app.storingway import engine


def add_batch(data: list[UniversalisEntry]):
    with Session(engine) as session:
        for d in data:
            session.add(d)
        session.commit()


def remove_by_item(item_id: int):
    with Session(engine) as session:
        session.query(UniversalisEntry).filter(UniversalisEntry.item_id == item_id).delete()
        session.commit()


def get_by_item(item_id: int):
    with Session(engine) as session:
        return session.query(UniversalisEntry).filter(UniversalisEntry.item_id == item_id).all()
