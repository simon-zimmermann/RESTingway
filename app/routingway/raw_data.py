from fastapi import Depends
from sqlalchemy.orm import Session
from fastapi import APIRouter
import pkgutil

from ..storingway import get_db, models

router = APIRouter(tags=["raw"])


def create_routing_def(model_class: any, schema_class: any):

    print("dynamically creating route for %s" % model_class.__name__)

    @router.get(f"/raw/{model_class.__name__}/", response_model=list[schema_class])
    def dynamic_raw_data(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
        kinds = db.query(model_class).offset(skip).limit(limit).all()
        ret = [kind.to_schema() for kind in kinds]
        return ret

    return dynamic_raw_data


def create_dynamic_routes():
    # Get list of all models in storingway/models
    for model_info in pkgutil.iter_modules(models.__path__):
        model_class = getattr(models, model_info.name)
        schema_class = getattr(model_class, "Schema")
        create_routing_def(model_class, schema_class)
