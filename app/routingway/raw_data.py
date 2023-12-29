from sqlalchemy.orm import Session
from fastapi import APIRouter
import pkgutil

from .. import util
from ..storingway import models, engine
from ..storingway.models.AchievementCategory import AchievementCategory
from ..storingway.models.AchievementKind import AchievementKind


router = APIRouter(tags=["raw"])


def create_routing_def(model_class: any):
    print("dynamically creating route for %s" % model_class.__name__)

    @router.get(f"/raw/{model_class.__name__}/")
    def dynamic_raw_data(skip: int = 0, limit: int = 100) -> list[model_class]:
        with Session(engine) as session:
            data = session.query(model_class).offset(skip).limit(limit).all()
            return data

    return dynamic_raw_data


@router.get("/test/jointest1/")
def dynamic_raw_data1():
    with Session(engine) as session:
        data = session.query(AchievementCategory).first()
        ret = data.model_dump()
        ret["achievement_kind"] = data.achievement_kind.model_dump()
        return ret


@router.get("/test/jointest2/")
def dynamic_raw_data2():
    with Session(engine) as session:
        data = session.query(AchievementCategory, AchievementKind).join(AchievementKind, isouter=True).offset(5).first()
        ret = data._asdict()
        return ret


def create_dynamic_routes():
    # Import all modules from storingway/models
    for model_info in pkgutil.iter_modules(models.__path__):
        imported_module = util.import_if_exists(model_info.name, "app.storingway.models")
        if not imported_module:
            raise ImportError("Could not dynamically import module %s" % model_info.name)
    # Get list of all models in storingway/models
    for model_info in pkgutil.iter_modules(models.__path__):
        imported_module = util.import_if_exists(model_info.name, "app.storingway.models")
        model_class = getattr(getattr(models, model_info.name), model_info.name)
        # schema_class = getattr(model_class, "Schema")
        # create_routing_def(model_class, schema_class)
        create_routing_def(model_class)


create_dynamic_routes()
