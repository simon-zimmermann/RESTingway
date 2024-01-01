import json
import os
import io
from camel_converter import to_snake

from . import csv_util
from ..config import config

from ..storingway import models_generated


class CSVColumnGenerator():

    def __init__(self, model_name: str, csv_colname: str, csv_datatype: str):
        self.model_name = model_name
        self.csv_datatype = csv_datatype
        self.py_colname = csv_util.convert_colname(csv_colname)
        self.py_datatype = csv_util.convert_datatype(csv_datatype)
        self.foreign_table = ""
        self.foreign_model = ""
        self.addedToParsingwayJson = False

    def generate(self, log_stream: io.StringIO) -> str:
        """Generates a model field based on the csv column name and datatype.
        Returns a string that can be written to a python model file."""
        model_field = ""

        # id column
        if (self.py_colname == "id"):
            model_field = f"    {self.py_colname}: int = Field(default=None, primary_key=True)\n"
        # Empty coulmn => skip
        elif (self.py_colname == ""):
            return ""
        # Primitive types
        elif (self.py_datatype == "int"):
            model_field = f"    {self.py_colname}: int\n"
        elif (self.py_datatype == "bool"):
            model_field = f"    {self.py_colname}: bool\n"
        elif (self.py_datatype == "str"):
            model_field = f"    {self.py_colname}: str\n"
        elif (self.py_datatype == "float"):
            model_field = f"    {self.py_colname}: float\n"
        # Foreign keys
        elif (self.py_datatype == "FOREIGN_KEY"):
            self.foreign_table = to_snake(self.csv_datatype)
            self.foreign_model = self.csv_datatype
            model_field = f"    {self.py_colname}_id: Optional[int] = Field(default=None, foreign_key=\"{self.foreign_table}.id\")\n" +\
                          f"    {self.py_colname}: Optional[\"{self.foreign_model}\"] = " +\
                          f"Relationship(sa_relationship_kwargs={{\"foreign_keys\": \"[{self.model_name}.{self.py_colname}_id]\"}})\n"

            # If the foreign model does not exist, add it to parsingway.json
            if not self.__model_file_exists(self.foreign_model):
                self.__add_to_parsingway_json(self.foreign_model, log_stream)

        return model_field

    def __add_to_parsingway_json(self, model_name: str, log_stream: io.StringIO):
        """Adds a model_name to parsingway.json for it to be loaded the next time."""
        with open(config.filepath_parsingway_json, "r+") as f:
            jsonfile = json.load(f)
            lst: list = jsonfile["csv"]["files_to_parse"]
            datatype_str = f"{model_name}.csv"
            # Don't add duplicates
            if datatype_str not in lst:
                print(f"Adding {model_name}.csv to parsingway.json.", file=log_stream)
                lst.append(datatype_str)
                jsonfile["csv"]["files_to_parse"] = lst
                f.seek(0)
                json.dump(jsonfile, f, indent=4)
                f.truncate()
                self.addedToParsingwayJson = True

    def __model_file_exists(self, model_name: str) -> bool:
        """Checks if a file named model_name.py exists in the models folder."""
        return os.path.exists(os.path.join(models_generated.__path__[0], model_name + ".py"))
