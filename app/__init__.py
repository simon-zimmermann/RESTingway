import importlib
from pydantic import BaseModel
from fastapi import FastAPI
import traceback

# pydantic config
BaseModel.model_config['protected_namespaces'] = ()

print("starting FastAPI...")
rest_app = FastAPI()

router_list = ["raw_data", "admin", "items", "universalis_data"]
for router in router_list:
    try:
        # Deveopment failsafe
        module = importlib.import_module(f".{router}", package="app.routes")
        if not module:
            print(f"Failed to import router {router}: it does not exist.")
        else:
            router_obj = getattr(module, "router")
            rest_app.include_router(router_obj)
    except Exception as e:
        print(f"Failed to import router {router}: {e}")
        traceback.print_exc()
        pass
