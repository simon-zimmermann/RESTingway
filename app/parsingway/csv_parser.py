import os
import csv
import io
from sqlalchemy.orm import Session
from types import ModuleType
from app.storingway import get_db
from ..config import config
from .csv_model_generator import CSVModelGenerator
from . import csv_util
from .. import util


class CSVParser:
    def __init__(self, csv_filename: str):
        self.csv_filename = csv_filename
        self.csv_filepath = os.path.join(config.path_gamedata_csv, csv_filename)
        self.model_name = self.csv_filename.split(".")[0]
        self.csv_colnames: list[str] = []
        self.csv_datatypes: list[str] = []
        self.imported_module: bool | ModuleType = False
        self.numGeneratedModels = 0
        self.numAddedToParsingwayJson = 0

        self.__csvfile = open(self.csv_filepath, newline="", encoding="utf-8")
        self.csvreader = csv.reader(self.__csvfile, delimiter=",", quotechar="\"")

    def __del__(self):
        self.__csvfile.close()

    def parse_header(self, log_stream: io.StringIO):
        print(f"Parsing header of CSV file {self.csv_filepath}", file=log_stream)
        (self.csv_colnames, self.csv_datatypes) = self.__read_header()

        # If debugging, it is possible to limit the number of columns added to the database, since there can be a lot.
        if (config.debug_limit_db_columns > 0):
            del self.csv_colnames[config.debug_limit_db_columns:]
            del self.csv_datatypes[config.debug_limit_db_columns:]

        # Check if the model class exists and is importable.
        self.imported_module = util.import_if_exists(self.model_name, "app.storingway.models")

        # If not, we need to generate the model class.
        if self.imported_module == False:
            print(f"Model class {self.model_name} does not exist. Generating it.", file=log_stream)
            generator = CSVModelGenerator(self.model_name, self.csv_colnames, self.csv_datatypes)
            generator.generate()
            self.numGeneratedModels += 1
            self.numAddedToParsingwayJson += generator.numAddedToParsingwayJson
            # Import the newly generated model class.
            self.imported_module = util.import_if_exists(self.model_name, "app.storingway.models")

    def parse_body(self, log_stream: io.StringIO):
        print(f"Parsing body of CSV file {self.csv_filepath}, adding to database.", file=log_stream)
        db: Session = next(get_db())
        if self.imported_module == False:
            raise RuntimeError(f"Model class {self.model_name} does not exist. Cannot parse body!")

        # For each line, build a dictionary.
        # Keys are the column names, values are the values in the csv file.
        for line_keydict in self.__read_file_byline():
            # print(line_keydict)
            model_class = getattr(self.imported_module, self.model_name)
            # Actually create the ORM object, initializing it with the values from the csv file.
            db_obj = model_class(**line_keydict)
            db.add(db_obj)

        db.commit()
        db.refresh(db_obj)

    def __read_header(self) -> (list[str], list[str]):
        indices = next(self.csvreader)
        colnames = next(self.csvreader)
        datatypes = next(self.csvreader)
        # check if indices are consistent. Failsafe for broken files.
        for i in range(len(indices)):
            if (i == 0) and ("key" in indices[i]):
                continue
            if int(indices[i]) + 1 == i:
                continue
            raise ValueError(f"CSV file {self.csv_filepath} could not be read."
                             f"Indices not consistent. Expected {i}, got {indices[i]}")
        return (colnames, datatypes)

    def __read_file_byline(self):
        for row in self.csvreader:
            # Debug option: make it faster
            if (config.debug_limit_db_rows > 0 and self.csvreader.line_num > config.debug_limit_db_rows):
                break
            keydict = {}
            for i in range(len(self.csv_colnames)):
                # ignore empty columns
                if (self.csv_colnames[i] == ""):
                    continue
                # Convert the string into a proper datatype.
                py_datatype = csv_util.convert_datatype(self.csv_datatypes[i])
                py_colname = csv_util.convert_colname(self.csv_colnames[i])
                converted_value = csv_util.convert_value(py_datatype, row[i])
                keydict[py_colname] = converted_value
            yield keydict
