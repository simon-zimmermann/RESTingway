import json
import os
import io

from app.storingway import models, TableBase, engine
from .csv_parser import CSVParser


def delete_models():
    path = models.__path__[0]
    print(f"Deleting all model files in {path}.")
    files: list[str] = os.listdir(models.__path__[0])
    for filename in files:
        if filename.endswith(".py") and filename != "__init__.py":
            os.remove(os.path.join(path, filename))


def delete_db():
    if (os.path.exists("sql_app.db")):
        os.remove("sql_app.db")


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
    TableBase.metadata.create_all(bind=engine)

    # Actually read the contents of the csv files and add them to the database.
    for parser in parser_list:
        parser.parse_body(log_stream)

    print("Successfully parsed CSV files.", file=log_stream)
    return numGeneratedModels, numAddedToParsingwayJson
