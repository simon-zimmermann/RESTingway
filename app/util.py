import importlib
from types import ModuleType


def import_if_exists(module: str, package: str) -> bool | ModuleType:
    try:
        return importlib.import_module(f".{module}", package=package)
    except ModuleNotFoundError:
        return False
