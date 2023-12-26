from fastapi import FastAPI

from . import parsingway
from .routingway import misc_routes, raw_data

print("reading csv files...")
parsingway.parse_all()

print("starting FastAPI...")
app = FastAPI()
app.include_router(misc_routes.router)
#raw_data.create_dynamic_routes()
app.include_router(raw_data.router)
