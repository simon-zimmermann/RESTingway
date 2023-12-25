import csv
from sqlalchemy.orm import Session
import json
import importlib
import os
from camel_converter import to_snake

from ..storingway import get_db, models
from ..config import config


def parse_all():
    with open("resources/parsingway.json") as f:
        d = json.load(f)
        for entry in d["csvparser"]:
            parse_single_csv(entry)


def convert_csv_name(csvname) -> str:
    if csvname == "#":
        return "id"
    else:
        return to_snake(csvname)


def convert_csv_datatype(datatype: str, value: str) -> any:
    if (datatype == "int32" or datatype == "byte"):
        if (value.isnumeric()):
            return int(value)
        else:
            return None
    elif (datatype == "str"):
        return value
    elif (datatype.startswith("bit&")):
        return value == "True"
    elif (value.isnumeric()):  # probably a id as a reference to another table
        return int(value)
    return None

# TODO: this should output python code with the correct class if insertion is not working
# def verify_data_types(keys, datatypes, db_model_class) -> bool:
#    schema_class = getattr(db_model_class, "Schema")
#    model_obj = db_model_class()
#    # schema_obj = schema_class()
#    for key in keys:
#        key = convert_csv_name(key)
#        try:
#            model_attr = getattr(model_obj, key)
#            # schema_attr = getattr(schema_obj, key)
#            print(type(model_attr))
#        except AttributeError:
#            print("key %s not found in %s" % (key, db_model_class))
#            return False
#    return True


def parse_single_csv(parsingway_entry):
    source_path = parsingway_entry["source_path"]
    filepath = os.path.join(config.path_gamedata_csv, source_path)
    db_model = parsingway_entry["db_model"]
    db_model_class = getattr(models, db_model)
    db: Session = next(get_db())
    print("Parsing csv file: %s" % source_path)

    try:
        with open(filepath) as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            _ = next(reader)  # this line containes the indices of the columns. not needed.
            colnames = next(reader)
            datatypes = next(reader)

            # Process column names, converting them to snake_case and fixing any other issues.
            fixed_colnames = [convert_csv_name(colname) for colname in colnames]
            # For each line, build a dictionary.
            # Keys are the column names, values are the values in the csv file.
            for row in reader:
                keydict = {}
                for i in range(len(fixed_colnames)):
                    # Convert the string into a proper datatype.
                    converted_value = convert_csv_datatype(datatypes[i], row[i])
                    keydict[fixed_colnames[i]] = converted_value

                # Actually create the ORM object, initializing it with the values from the csv file.
                db_obj = db_model_class(**keydict)
                db.add(db_obj)

            db.commit()
            db.refresh(db_obj)
    except Exception as e:
        print("error while adding entry from csv file %s. Exception is %s" % (source_path, e))
        pass
