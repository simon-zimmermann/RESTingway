from fastapi import FastAPI
from pydantic import BaseModel
import traceback

from . import util

# Pydantic config
BaseModel.model_config['protected_namespaces'] = ()

print("starting FastAPI...")
app = FastAPI()

# Only include routers for which all required modules are available.
router_list = ["misc_routes", "raw_data", "admin", "items", "universalis_import"]
for router in router_list:
    try:
        module = util.import_if_exists(router, "app.routingway")
        router_obj = getattr(module, "router")
        app.include_router(router_obj)
    except Exception as e:
        print(f"Failed to include router {router}: {e}")
        traceback.print_exc()
        pass
