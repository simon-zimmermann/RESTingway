from fastapi import APIRouter
import pkgutil
from sqlmodel import Session, select

from app import util
from app.storingway import models_generated, models, engine


router = APIRouter(tags=["raw"])


def create_routing_def(model_class: any):
    @router.get(f"/raw/{model_class.__name__}/")
    def dynamic_raw_data(offset: int = 0, limit: int = 100) -> list[model_class]:
        with Session(engine) as session:
            statement = select(model_class).offset(offset).limit(limit)
            data = session.exec(statement).all()
            return data

    return dynamic_raw_data


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
