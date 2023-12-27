import csv
import json
import traceback
import os
import re
import importlib

from ..config import config
from app.storingway import models, TableBase, engine
from .csv_parser import CSVParser


def parse_all():
    #try:
    if (config.delete_models_on_startup):
        path = models.__path__[0]
        print(f"Deleting all model files in {path}.")
        files: list[str] = os.listdir(models.__path__[0])
        for filename in files:
            if filename.endswith(".py") and filename != "__init__.py":
                os.remove(os.path.join(path, filename))
        if (os.path.exists("sql_app.db")):
            os.remove("sql_app.db")

    # Parse headers, create model classes
    parser_list: list[CSVParser] = []
    with open("resources/parsingway.json") as f:
        d = json.load(f)
        for entry in d["csvparser"]:
            parser = CSVParser(entry)
            parser.parse_header()
            parser_list.append(parser)

    TableBase.metadata.create_all(bind=engine)

    for parser in parser_list:
        parser.parse_body()

    #except Exception as e:
    #    print("error while parsing csv files. Exception is: \n%s" % e)
    #    traceback.print_exc()
