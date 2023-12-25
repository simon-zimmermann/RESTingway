from fastapi import FastAPI

from . import parsingway
from .routingway import misc_routes

print("reading csv files...")
parsingway.parse_all()

print("starting FastAPI...")
app = FastAPI()
app.include_router(misc_routes.router)
