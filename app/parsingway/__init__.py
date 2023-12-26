import csv
from sqlalchemy.orm import Session
import json
import traceback
import os
import re
import importlib
from types import ModuleType

from ..config import config
from .csv_model_generator import CSVModelGenerator


def parse_all():
    max_retries = 20
    for i in range(max_retries):
        with open("resources/parsingway.json") as f:
            d = json.load(f)
            created_code = False
            print(f"Starting parsingway iteration {i}")
            for entry in d["csvparser"]:
                if parse_single_csv(entry):
                    created_code = True
            if not created_code:
                return


def check_model_class(colnames: list[str], model_class: any) -> bool:
    model_obj = model_class()
    for colname in colnames:
        # ignore empty columns
        if colname == "":
            continue
        try:
            getattr(model_obj, colname)
        except AttributeError:
            print("key %s not found in %s" % (colname, model_class))
            return False
    return True


def import_if_model_exists(model_name: str) -> bool | ModuleType:
    try:
        return importlib.import_module(f".{model_name}", package="app.storingway.models")
    except ModuleNotFoundError:
        # traceback.print_exc()
        return False


def parse_single_csv(csv_filename: str) -> bool:
    filepath = os.path.join(config.path_gamedata_csv, csv_filename)
    db_model = csv_filename.split(".")[0]
    # db: Session = next(get_db())
    print("Parsing csv file: %s" % csv_filename)

    try:
        with open(filepath, encoding="utf8") as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            _ = next(reader)  # this line containes the indices of the columns. not needed.
            csv_colnames = next(reader)
            csv_datatypes = next(reader)

            # Process column names, converting them to snake_case and fixing any other issues.
            # colnames = [sanitize_colnames(colname) for colname in colnames]

            imported_module = import_if_model_exists(db_model)

            if imported_module == False:
                print(f"Model class {db_model} does not exist. Generating it.")
                CSVModelGenerator(db_model, csv_colnames, csv_datatypes).generate()
                return True

            # db_model_class = getattr(imported_module, db_model)

            # Check if the model class has all the columns that are in the csv file.
            # if not check_model_class(colnames, db_model_class):
            #    print(f"Model class {db_model_class} does not match the csv file {csv_filename}.")
            #    # print("Trying to generate new model class!")
            #    # generate_model_class(colnames, datatypes, db_model)
            #    return False

            # For each line, build a dictionary.
            # Keys are the column names, values are the values in the csv file.
            # for row in reader:
            #    keydict = {}
            #    for i in range(len(colnames)):
            #        # ignore empty columns
            #        # TODO maby not ignore empty columns
            #        if (colnames[i] == ""):
            #            continue
            #        # Convert the string into a proper datatype.
            #        converted_value = convert_csv_datatype(datatypes[i], row[i])
            #        keydict[colnames[i]] = converted_value

                # Actually create the ORM object, initializing it with the values from the csv file.
                # db_obj = db_model_class(**keydict)
                # db.add(db_obj)

            # db.commit()
            # db.refresh(db_obj)
    except Exception as e:
        print("error while adding entry from csv file %s. Exception is: \n%s" % (csv_filename, e))
        traceback.print_exc()
        pass

    return False
