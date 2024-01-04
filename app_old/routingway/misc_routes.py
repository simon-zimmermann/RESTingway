from fastapi import APIRouter

from app import config


router = APIRouter(tags=["misc"])


@router.get("/info/", response_model=config.Config)
def info():
    return config.config
