import json
import os
import io
import sys
from sqlmodel import SQLModel


from .csv_parser import CSVParser

from app.db import models_generated, engine
from app.common import config


def delete_generated_models(log_stream: io.StringIO):
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


def parse_csv(log_stream: io.StringIO) -> (int, int, int):
    print("Parsing CSV files.", file=log_stream)
    # Parse headers, create model classes. Save Parsers for later.
    parser_list: list[CSVParser] = []
    numGeneratedModels = 0
    numAddedToJsonConfig = 0
    rowsInserted = 0
    with open(config.filepath_gamedata_parser_json) as f:
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
                numAddedToJsonConfig += parser.numAddedToJsonConfig

    print("Successfully parsed headers of CSV files.", file=log_stream)

    if numAddedToJsonConfig > 0:
        print("Cannot parse csv bodies, since new models have been added to gamedata_parser.json.")
    else:
        # Re-create all tables to match with model definitions.
        SQLModel.metadata.create_all(engine)
        # Actually read the contents of the csv files and add them to the database.
        for parser in parser_list:
            parser.parse_body(log_stream)
            rowsInserted += parser.rowsInserted

        print("Successfully parsed bodies of CSV files.", file=log_stream)
    return numGeneratedModels, numAddedToJsonConfig, rowsInserted
