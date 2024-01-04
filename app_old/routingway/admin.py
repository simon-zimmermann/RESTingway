from fastapi import APIRouter
import traceback
import io
from sqlmodel import SQLModel, Session, delete

from . import responses as r

from app import util
from app.parsingway import parsingway
from app.storingway import engine


router = APIRouter(tags=["admin"])


@router.patch("/admin/recreate/all")
def recreate_all() -> r.LogResponse:
    log_stream = io.StringIO()
    try:
        parsingway.delete_models(log_stream)
        (numGeneratedModels, numAddedToParsingwayJson, rowsInserted) = parsingway.parse_csv(log_stream)
        report = {
            "numGeneratedModels": numGeneratedModels,
            "numAddedToParsingwayJson": numAddedToParsingwayJson,
            "rowsInserted": rowsInserted
        }
        print("Recreation complete, program will be restarted in 3 sec.", file=log_stream)
        # we need to stop the app, because sqlalchemy cant handle this
        util.stop_app(3)
        return r.LogResponse(log=log_stream.getvalue().splitlines(), report=report)
    except Exception as e:
        print(traceback.format_exc(), file=log_stream)
        return r.LogResponse(log=log_stream.getvalue().splitlines(), success=False, status=str(e))
    finally:
        log_stream.close()


@router.patch("/admin/recreate/non_dynamic")
def recreate_non_dynamic():
    # TODO make this dynamic
    from app.storingway.models.UniversalisEntry import UniversalisEntry
    SQLModel.metadata.drop_all(engine, tables=[UniversalisEntry.__table__])
    SQLModel.metadata.create_all(engine)
