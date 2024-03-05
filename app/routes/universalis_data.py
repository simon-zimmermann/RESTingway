from fastapi import APIRouter, BackgroundTasks
from app.routes.responses import BasicResponse

from app.universalis_scraper.scraper import refresh_universalis_data
from app.calc.market_prices import test_average_calc

router = APIRouter(tags=["universalis"])


@router.patch("/universalis/start_cycle")
def universalis_start_cycle(background_tasks: BackgroundTasks) -> BasicResponse:
    background_tasks.add_task(refresh_universalis_data)
    return BasicResponse(status="Universalis refresh cycle started.")


@router.get("/universalis/calc_test")
def universalis_calc_test() -> BasicResponse:
    test_result_str = test_average_calc()
    return BasicResponse(status="Test complete.", report=test_result_str)
