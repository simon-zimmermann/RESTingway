from fastapi import Depends
from sqlalchemy.orm import Session
from fastapi import APIRouter
import pkgutil

from ..storingway import get_db, models
from .. import util
import app.routingway.responses as r

router = APIRouter(tags=["raw"])


def create_routing_def(model_class: any, schema_class: any):

    print("dynamically creating route for %s" % model_class.__name__)

    @router.get(f"/raw/{model_class.__name__}/")
    def dynamic_raw_data(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)) -> r.RawDataResponse:
        data = db.query(model_class).offset(skip).limit(limit).all()
        count_total = db.query(model_class).count()
        count_data = len(data)
        data_schema = [d.to_schema() for d in data]
        # TODO this is stupid. the actual schema object (as dynamically created) should be returned, not a dict of it
        data_dict = [d.dict() for d in data_schema]
        return r.RawDataResponse(results=data_dict, results_returned=count_data, results_total=count_total)

    return dynamic_raw_data


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
        schema_class = getattr(model_class, "Schema")
        create_routing_def(model_class, schema_class)
