from fastapi import APIRouter
from sys import stdout
import traceback
import io
from sqlmodel import SQLModel

from app.routes.responses import LogResponse
from app.common import util, config
from app.db import engine


router = APIRouter(tags=["admin"])


@router.patch("/admin/clear_database")
def admin_clear_database() -> LogResponse:
    log_stream = io.StringIO()
    print("deleting all generated models and clearing the database", file=log_stream)
    try:
        from app.gamedata_parser.parser import delete_generated_models
        # First delete all generated models
        delete_generated_models(stdout)

        # Then delete all tables, and remove any references to them.
        # This is enough to re-create and re-import the tables/data, but the program still needs to be restarted.
        print("Deleting all tables, and removing all references, mappers and registries.", file=log_stream)
        SQLModel.metadata.drop_all(engine)
        SQLModel.metadata.clear()

        print("Deletion complete, program will be stopped in 3 sec.", file=log_stream)
        # we need to stop the app, because sqlalchemy cant handle this
        util.stop_app(3)
        return LogResponse(log=log_stream.getvalue().splitlines())
    except Exception as e:
        print(traceback.format_exc(), file=log_stream)
        return LogResponse(log=log_stream.getvalue().splitlines(), success=False, status=str(e))
    finally:
        log_stream.close()


@router.patch("/admin/parse_gamedata")
def admin_parse_gamedata() -> LogResponse:
    log_stream = io.StringIO()
    print("running gamedata_parser", file=log_stream)
    try:
        from app.gamedata_parser.parser import parse_csv
        (numGeneratedModels, numAddedToParsingwayJson, rowsInserted) = parse_csv(log_stream)
        report = {
            "numGeneratedModels": numGeneratedModels,
            "numAddedToParsingwayJson": numAddedToParsingwayJson,
            "rowsInserted": rowsInserted
        }
        print("Recreation complete, program will be stopped in 3 sec.", file=log_stream)
        # we need to stop the app, because sqlalchemy cant handle this
        util.stop_app(3)
        return LogResponse(log=log_stream.getvalue().splitlines(), report=report)
    except Exception as e:
        print(traceback.format_exc(), file=log_stream)
        return LogResponse(log=log_stream.getvalue().splitlines(), success=False, status=str(e))
    finally:
        log_stream.close()


@router.get("/admin/config/", response_model=config)
def admin_config():
    return config
