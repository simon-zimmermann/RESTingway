import csv
from sqlalchemy.orm import Session
import json
import traceback
import os
import re
import importlib
from types import ModuleType
from camel_converter import to_snake

from ..storingway import get_db, models
from ..config import config

# TODO: automatically create the models in storingway/models from the csv files (create pyhton code)


def parse_all():
    with open("resources/parsingway.json") as f:
        d = json.load(f)
        for entry in d["csvparser"]:
            parse_single_csv(entry)


def sanitize_colnames(csvname) -> str:
    if csvname == "#":
        return "id"
    else:
        # Remove invalid characters
        fixed_name = re.sub('[^0-9a-zA-Z_]', '', csvname)
        # Remove leading characters until we find a letter or underscore
        fixed_name = re.sub('^[^a-zA-Z_]+', '', fixed_name)
        return to_snake(fixed_name)


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
    except ModuleNotFoundError as e:
        print("Model class %s does not exist." % model_name)
        # traceback.print_exc()

        return False


def generate_model_class(colnames: list[str], datatypes: list[str], model_name: str):
    model_fileds = ""
    schema_fields = ""
    import_list = []
    for i in range(len(colnames)):
        colname = colnames[i]
        datatype = datatypes[i]
        # Handle special cases
        # First special columns, second all primitive types, third foreign keys
        if (colname == "id"):
            model_fileds += f"    {colname}: Mapped[int] = mapped_column(primary_key=True, index=True)\n"
            schema_fields += f"        {colname}: int\n"
        # ignore empty columns
        elif (colname == ""):
            pass
        # data types
        elif (datatype.startswith("bit&")):
            model_fileds += f"    {colname}: Mapped[bool] = mapped_column()\n"
            schema_fields += f"        {colname}: bool\n"
        elif (datatype == "int32" or datatype == "byte"):
            model_fileds += f"    {colname}: Mapped[int] = mapped_column()\n"
            schema_fields += f"        {colname}: int\n"
        elif (datatype == "uint16"):
            model_fileds += f"    {colname}: Mapped[int] = mapped_column()\n"
            schema_fields += f"        {colname}: int\n"
        elif (datatype == "str"):
            model_fileds += f"    {colname}: Mapped[str] = mapped_column()\n"
            schema_fields += f"        {colname}: str\n"
        elif (datatype == "sbyte"):
            model_fileds += f"    {colname}: Mapped[int] = mapped_column()\n"
            schema_fields += f"        {colname}: int\n"
        elif (datatype == "uint32"):
            model_fileds += f"    {colname}: Mapped[int] = mapped_column()\n"
            schema_fields += f"        {colname}: int\n"
        elif (datatype == "int64"):
            model_fileds += f"    {colname}: Mapped[int] = mapped_column()\n"
            schema_fields += f"        {colname}: int\n"
        elif (datatype == "int16"):
            model_fileds += f"    {colname}: Mapped[int] = mapped_column()\n"
            schema_fields += f"        {colname}: int\n"
        elif (datatype == "bool"):
            model_fileds += f"    {colname}: Mapped[bool] = mapped_column()\n"
            schema_fields += f"        {colname}: bool\n"
        elif (datatype == "Image"):
            model_fileds += f"    {colname}: Mapped[int] = mapped_column()\n"
            schema_fields += f"        {colname}: int\n"
        elif (datatype == "Row"):
            model_fileds += f"    {colname}: Mapped[int] = mapped_column()\n"
            schema_fields += f"        {colname}: int\n"
        elif (datatype == "single"):
            model_fileds += f"    {colname}: Mapped[int] = mapped_column()\n"
            schema_fields += f"        {colname}: int\n"
        elif (datatype == "Color"):
            model_fileds += f"    {colname}: Mapped[int] = mapped_column()\n"
            schema_fields += f"        {colname}: int\n"
        # foreign keys
        else:
            #if (model_name == datatype):
            #    print("TODO: Self referencing foreign key %s" % colname)
            #    continue
            model_fileds += f"    {colname}: Mapped[int] = mapped_column(ForeignKey(\"{to_snake(datatype)}.id\"))\n"
            # model_fileds += f"    {colname}_obj: Mapped[{datatype}.{datatype}] = relationship({datatype}.{datatype}, foreign_keys='{model_name}.{colname}')\n"
            # model_fileds += f"    {colname}_obj: Mapped\n"
            schema_fields += f"        {colname}: {datatype}.{datatype}.Schema\n"
            if datatype not in import_list and datatype != model_name:
                import_list.append(datatype)
            # check if forein key has a associated model class
            if not hasattr(models, datatype):
                with open("resources/parsingway.json", "r+") as f:
                    jsonfile = json.load(f)
                    lst: list = jsonfile["csvparser"]
                    datatype_str = f"{datatype}.csv"
                    if datatype_str not in lst:
                        print(f"Model class {datatype} does not exist.")
                        print(f"Adding {datatype}.csv to parsingway.json!")
                        lst.append(datatype_str)
                        jsonfile["csvparser"] = lst
                        f.seek(0)
                        json.dump(jsonfile, f, indent=4)
                        f.truncate()

    import_string = "\n".join([f"import app.storingway.models.{datatype} as {datatype}" for datatype in import_list])

    generated_code = f'''from __future__ import annotations
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from pydantic import BaseModel

from .. import TableBase

{import_string}

class {model_name}(TableBase):


    __tablename__ = "{to_snake(model_name)}"
    __allow_unmapped__ = True
{model_fileds}

        '''  # class Schema(BaseModel):
# {schema_fields}

    new_filename = os.path.join(models.__path__[0], model_name + ".py")
    with open(new_filename, "w") as f:
        f.write(generated_code)

    print("Generated new model class %s" % model_name)


def parse_single_csv(csv_filename: str) -> bool:
    filepath = os.path.join(config.path_gamedata_csv, csv_filename)
    db_model = csv_filename.split(".")[0]
    db: Session = next(get_db())
    print("Parsing csv file: %s" % csv_filename)

    try:
        with open(filepath, encoding="utf8") as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            _ = next(reader)  # this line containes the indices of the columns. not needed.
            colnames = next(reader)
            datatypes = next(reader)

            # Process column names, converting them to snake_case and fixing any other issues.
            colnames = [sanitize_colnames(colname) for colname in colnames]

            imported_module = import_if_model_exists(db_model)

            if imported_module == False:
                print(f"Model class {db_model} does not exist.")
                print("Trying to generate new model class!")
                generate_model_class(colnames, datatypes, db_model)
                return True

            db_model_class = getattr(imported_module, db_model)

            # Check if the model class has all the columns that are in the csv file.
            if not check_model_class(colnames, db_model_class):
                print(f"Model class {db_model_class} does not match the csv file {csv_filename}.")
                # print("Trying to generate new model class!")
                # generate_model_class(colnames, datatypes, db_model)
                return False

            # For each line, build a dictionary.
            # Keys are the column names, values are the values in the csv file.
            for row in reader:
                keydict = {}
                for i in range(len(colnames)):
                    # ignore empty columns
                    # TODO maby not ignore empty columns
                    if (colnames[i] == ""):
                        continue
                    # Convert the string into a proper datatype.
                    converted_value = convert_csv_datatype(datatypes[i], row[i])
                    keydict[colnames[i]] = converted_value

                # Actually create the ORM object, initializing it with the values from the csv file.
                db_obj = db_model_class(**keydict)
                # db.add(db_obj)

            # db.commit()
            # db.refresh(db_obj)
    except Exception as e:
        print("error while adding entry from csv file %s. Exception is: \n%s" % (csv_filename, e))
        traceback.print_exc()
        pass

    return False
