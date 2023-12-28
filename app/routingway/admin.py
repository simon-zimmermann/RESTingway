from fastapi import APIRouter, status
import traceback
import io
from ..parsingway import parsingway
import app.routingway.responses as r

router = APIRouter(tags=["admin"])


@router.delete("/admin/database", status_code=status.HTTP_200_OK)
def delete_db() -> r.BasicResponse:
    parsingway.delete_db()
    return r.BasicResponse()


@router.delete("/admin/models")
def delete_models() -> r.BasicResponse:
    parsingway.delete_models()
    return r.BasicResponse()


@router.patch("/admin/recreate/all")
def recreate_all() -> r.LogResponse:
    log_stream = io.StringIO()
    try:
        parsingway.delete_db()
        parsingway.delete_models()
        (numGeneratedModels, numAddedToParsingwayJson) = parsingway.parse_all(log_stream)
        report = {
            "numGeneratedModels": numGeneratedModels,
            "numAddedToParsingwayJson": numAddedToParsingwayJson
        }
        return r.LogResponse(log=log_stream.getvalue().splitlines(), report=report)
    except Exception as e:
        print(traceback.format_exc(), file=log_stream)
        return r.LogResponse(log=log_stream.getvalue().splitlines(), success=False, status=str(e))
    finally:
        log_stream.close()
