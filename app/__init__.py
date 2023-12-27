from fastapi import FastAPI
from pydantic import BaseModel

from . import parsingway
from .routingway import misc_routes, raw_data
from app.storingway import models, TableBase, engine

# Pydantic config
BaseModel.model_config['protected_namespaces'] = ()

print("reading csv files...")
parsingway.parse_all()


print("starting FastAPI...")
app = FastAPI()
app.include_router(misc_routes.router)
# raw_data.create_dynamic_routes()
app.include_router(raw_data.router)
