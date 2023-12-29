import json
import os
import io
import sys
from sqlmodel import SQLModel
from sqlalchemy import orm

from .csv_parser import CSVParser
from ..storingway import models, engine


def delete_models(log_stream: io.StringIO):
    # First unload all modules
    print("Unloading all model modules.", file=log_stream)
    for module in list(sys.modules.keys()):
        if module.startswith("app.storingway.models"):
            del sys.modules[module]
    # Then delete all model files
    path = models.__path__[0]
    print(f"Deleting all model files in {path}.", file=log_stream)
    files: list[str] = os.listdir(models.__path__[0])
    for filename in files:
        if filename.endswith(".py") and filename != "__init__.py":
            os.remove(os.path.join(path, filename))

    # Then delete all tables, and remove any references to them.
    # This is enough to re-create and re-import the tables/data, but the program still needs to be restarted.
    print("Deleting all tables, and removing all references, mappers and registries.", file=log_stream)
    SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.clear()
    orm.clear_mappers()


def parse_all(log_stream: io.StringIO) -> (int, int):
    numGeneratedModels = 0
    numAddedToParsingwayJson = 0
    print("Parsing all gamedata.", file=log_stream)
    (csv_genm, csv_addp) = parse_csv(log_stream)
    numGeneratedModels += csv_genm
    numAddedToParsingwayJson += csv_addp
    print("Successfully parsed all gamedata.", file=log_stream)
    return numGeneratedModels, numAddedToParsingwayJson


def parse_csv(log_stream: io.StringIO) -> (int, int):
    print("Parsing CSV files.", file=log_stream)
    # Parse headers, create model classes. Save Parsers for later.
    parser_list: list[CSVParser] = []
    numGeneratedModels = 0
    numAddedToParsingwayJson = 0
    with open("resources/parsingway.json") as f:
        d = json.load(f)
        for entry in d["csvparser"]:
            parser = CSVParser(entry)
            parser.parse_header(log_stream)
            parser_list.append(parser)
            numGeneratedModels += parser.numGeneratedModels
            numAddedToParsingwayJson += parser.numAddedToParsingwayJson

    # Create tables if new models were generated.
    # TableBase.metadata.create_all(bind=engine)
    SQLModel.metadata.create_all(engine)

    # Actually read the contents of the csv files and add them to the database.
    for parser in parser_list:
        parser.parse_body(log_stream)

    print("Successfully parsed CSV files.", file=log_stream)
    return numGeneratedModels, numAddedToParsingwayJson
