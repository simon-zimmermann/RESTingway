from fastapi import Depends
from sqlalchemy.orm import Session
from fastapi import APIRouter

from ..storingway import get_db, models
from .. import config


router = APIRouter(tags=["misc"])

# TODO dynamically create the routes for the raw csv data
@router.get("/achievement_kinds/", response_model=list[models.AchievementKind.Schema])
def achievement_kinds(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    kinds = db.query(models.AchievementKind).offset(skip).limit(limit).all()
    ret = [kind.to_schema() for kind in kinds]
    return ret


@router.get("/achievement_categories/", response_model=list[models.AchievementCategory.Schema])
def achievement_categories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    categories = db.query(models.AchievementCategory).offset(skip).limit(limit).all()
    ret = [category.to_schema() for category in categories]
    return ret

@router.get("/achievement_targets/", response_model=list[models.AchievementTarget.Schema])
def achievement_targets(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    targets = db.query(models.AchievementTarget).offset(skip).limit(limit).all()
    ret = [target.to_schema() for target in targets]
    return ret


@router.get("/info/", response_model=config.Config)
def info():
    return config.config
