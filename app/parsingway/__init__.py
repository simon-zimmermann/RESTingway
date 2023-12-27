import csv
from sqlalchemy.orm import Session
import json
import traceback
import os
import re
import importlib

from ..config import config
from app.storingway import models
from .csv_parser import CSVParser


def parse_all():
    if (config.delete_models_on_startup):
        path = models.__path__[0]
        print(f"Deleting all model files in {path}.")
        files: list[str] = os.listdir(models.__path__[0])
        for filename in files:
            if filename.endswith(".py") and filename != "__init__.py":
                os.remove(os.path.join(path, filename))

    max_retries = 20
    for i in range(max_retries):
        with open("resources/parsingway.json") as f:
            d = json.load(f)
            generated_code = False
            print(f"Starting parsingway iteration {i}")
            for entry in d["csvparser"]:
                parser = CSVParser(entry)
                success = parser.parse()
                if not success:
                    print(f"CSVParser: failed to parse {entry}")
                    break
                if parser.isFileGenerated:
                    generated_code = True
            if not generated_code:
                return
