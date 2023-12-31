from sqlalchemy.orm import Session
from fastapi import APIRouter
import pkgutil

from .. import util
from ..storingway import models_generated, models, engine
from ..storingway.models_generated.AchievementCategory import AchievementCategory
from ..storingway.models_generated.AchievementKind import AchievementKind


router = APIRouter(tags=["raw"])


def create_routing_def(model_class: any):
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
    # Import all modules from storingway/models_generated
    for model_info in pkgutil.iter_modules(models_generated.__path__):
        imported_module = util.import_if_exists(model_info.name, models_generated.__package__)
        if not imported_module:
            raise ImportError("Could not dynamically import module %s" % model_info.name)
    # Get list of all models in storingway/models_generated
    for model_info in pkgutil.iter_modules(models_generated.__path__):
        imported_module = util.import_if_exists(model_info.name, models_generated.__package__)
        model_class = getattr(getattr(models_generated, model_info.name), model_info.name)
        create_routing_def(model_class)

    # Import all modules from storingway/models
    for model_info in pkgutil.iter_modules(models.__path__):
        imported_module = util.import_if_exists(model_info.name, models.__package__)
        if not imported_module:
            raise ImportError("Could not dynamically import module %s" % model_info.name)
    # Get list of all models in storingway/models
    for model_info in pkgutil.iter_modules(models.__path__):
        imported_module = util.import_if_exists(model_info.name, models.__package__)
        model_class = getattr(getattr(models, model_info.name), model_info.name)
        create_routing_def(model_class)


create_dynamic_routes()
