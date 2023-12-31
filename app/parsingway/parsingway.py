import json
import os
import io
import sys
from sqlmodel import SQLModel
from sqlalchemy import orm

from .csv_parser import CSVParser
from ..storingway import models_generated, engine
from ..config import config


def delete_models(log_stream: io.StringIO):
    # First unload all modules
    print("Unloading all model modules.", file=log_stream)
    for module in list(sys.modules.keys()):
        if module.startswith("app.storingway.models"):
            del sys.modules[module]
    # Then delete all model files
    path = models_generated.__path__[0]
    print(f"Deleting all model files in {path}.", file=log_stream)
    files: list[str] = os.listdir(models_generated.__path__[0])
    for filename in files:
        if filename.endswith(".py") and filename != "__init__.py":
            os.remove(os.path.join(path, filename))

    # Then delete all tables, and remove any references to them.
    # This is enough to re-create and re-import the tables/data, but the program still needs to be restarted.
    print("Deleting all tables, and removing all references, mappers and registries.", file=log_stream)
    SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.clear()
    orm.clear_mappers()


def parse_all(log_stream: io.StringIO) -> (int, int, int):
    numGeneratedModels = 0
    numAddedToParsingwayJson = 0
    rowsInserted = 0
    print("Parsing all gamedata.", file=log_stream)
    (csv_genm, csv_addp, csv_addrow) = parse_csv(log_stream)
    numGeneratedModels += csv_genm
    numAddedToParsingwayJson += csv_addp
    rowsInserted += csv_addrow
    print("Successfully parsed all gamedata.", file=log_stream)
    return numGeneratedModels, numAddedToParsingwayJson, rowsInserted


def parse_csv(log_stream: io.StringIO) -> (int, int, int):
    print("Parsing CSV files.", file=log_stream)
    # Parse headers, create model classes. Save Parsers for later.
    parser_list: list[CSVParser] = []
    numGeneratedModels = 0
    numAddedToParsingwayJson = 0
    rowsInserted = 0
    with open(config.parsingway_json_filepath) as f:
        d = json.load(f)
        manual_fixes: list[dict] = d["csv"]["manual_fixes"]
        for entry in d["csv"]["files_to_parse"]:
            parser = CSVParser(entry, manual_fixes)
            parser_list.append(parser)

            model_exists = parser.parse_header(log_stream)
            if not model_exists:
                print(f"Model class {parser.model_name} does not exist. Generating it.", file=log_stream)
                parser.generate_model(log_stream)
                numGeneratedModels += parser.numGeneratedModels
                numAddedToParsingwayJson += parser.numAddedToParsingwayJson

    # Create tables if new models were generated.
    SQLModel.metadata.create_all(engine)

    # Actually read the contents of the csv files and add them to the database.
    for parser in parser_list:
        parser.parse_body(log_stream)
        rowsInserted += parser.rowsInserted

    print("Successfully parsed CSV files.", file=log_stream)
    return numGeneratedModels, numAddedToParsingwayJson, rowsInserted
