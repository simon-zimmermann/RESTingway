from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
import csv

from .storingway import get_db, models


app = FastAPI()

# load csv into database


@app.get("/admin/read_csv")
def read_csv(db: Session = Depends(get_db)):
    with open("gamedata/ffxiv-datamining/csv/AchievementKind.csv") as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        indices = next(reader)
        keys = next(reader)
        datatypes = next(reader)

        print("indices: %s" % indices)
        print("keys: %s" % keys)
        print("datatypes: %s" % datatypes)

        for row in reader:
            db_achievement_kind = models.AchievementKind(csv_row=row)
            db.add(db_achievement_kind)
        db.commit()
        db.refresh(db_achievement_kind)

    with open("gamedata/ffxiv-datamining/csv/AchievementCategory.csv") as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        indices = next(reader)
        keys = next(reader)
        datatypes = next(reader)

        print("indices: %s" % indices)
        print("keys: %s" % keys)
        print("datatypes: %s" % datatypes)

        for row in reader:
            db_achievement_category = models.AchievementCategory(csv_row=row)
            db.add(db_achievement_category)
        db.commit()
        db.refresh(db_achievement_category)


@app.get("/achievement_kinds/", response_model=list[models.AchievementKind.Schema])
def achievement_kinds(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    kinds = db.query(models.AchievementKind).offset(skip).limit(limit).all()
    ret = [kind.to_schema() for kind in kinds]
    return ret


@app.get("/achievement_categories/", response_model=list[models.AchievementCategory.Schema])
def achievement_categories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    categories = db.query(models.AchievementCategory).offset(skip).limit(limit).all()
    ret = [category.to_schema() for category in categories]
    return ret
