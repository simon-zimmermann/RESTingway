import os
import csv
import traceback

from ..config import config
from .csv_model_generator import CSVModelGenerator
from . import csv_util
from .. import util


class CSVParser:
    def __init__(self, csv_filename: str):
        self.csv_filename = csv_filename
        self.csv_filepath = os.path.join(config.path_gamedata_csv, csv_filename)
        self.model_name = self.csv_filename.split(".")[0]
        self.isFileGenerated = False

        self.__csvfile = open(self.csv_filepath, newline="", encoding="utf-8")
        self.csvreader = csv.reader(self.__csvfile, delimiter=",", quotechar="\"")

    def __del__(self):
        self.__csvfile.close()

    def parse(self) -> bool:
        print(f"Parsing CSV file {self.csv_filepath}")
        try:
            # db: Session = next(get_db())
            (csv_colnames, csv_datatypes) = self.__read_header()

            # Check if the model class exists and is importable.
            imported_module = util.import_if_exists(self.model_name, "app.storingway.models")

            # If not, we need to generate the model class.
            if imported_module == False:
                print(f"Model class {self.model_name} does not exist. Generating it.")
                CSVModelGenerator(self.model_name, csv_colnames, csv_datatypes).generate()
                self.isFileGenerated = True
                return True

            # TODO: make this work. probably by using real data from the first line, or removing this check.
            # If a model class exists, check if it matches the structure of the csv file.
            model_class = getattr(imported_module, self.model_name)
            # if not self.__verify_model_class(csv_colnames, model_class):
            #    print(f"Model class {model_class} does not match the csv file {self.csv_filename}.")
            #    print("Trying to generate new model class!")
            #    CSVModelGenerator(self.model_name, csv_colnames, csv_datatypes).generate()
            #    self.isFileGenerated = True
            #    return True

            # For each line, build a dictionary.
            # Keys are the column names, values are the values in the csv file.
            # for row in reader:
            #   keydict = {}
            #   for i in range(len(colnames)):
            #       # ignore empty columns
            #       # TODO maby not ignore empty columns
            #       if (colnames[i] == ""):
            #           continue
            #       # Convert the string into a proper datatype.
            #       converted_value = convert_csv_datatype(datatypes[i], row[i])
            #       keydict[colnames[i]] = converted_value
            for line_keydict in self.__read_file_byline(csv_colnames, csv_datatypes):
                #print(line_keydict)
                db_obj = model_class(**line_keydict)
                # Actually create the ORM object, initializing it with the values from the csv file.
                # db_obj = db_model_class(**keydict)
                # db.add(db_obj)

            # db.commit()
            # db.refresh(db_obj)
        except Exception as e:
            print("error while adding entry from csv file %s. Exception is: \n%s" % (self.csv_filepath, e))
            traceback.print_exc()
            return False
        return True

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

    def __read_file_byline(self, csv_colnames: list[str], csv_datatypes: list[str]):
        for row in self.csvreader:
            keydict = {}
            for i in range(len(csv_colnames)):
                # ignore empty columns
                # TODO maby not ignore empty columns
                if (csv_colnames[i] == ""):
                    continue
                # Convert the string into a proper datatype.
                py_datatype = csv_util.convert_datatype(csv_datatypes[i])
                py_colname = csv_util.convert_colname(csv_colnames[i])
                converted_value = csv_util.convert_value(py_datatype, row[i])
                keydict[py_colname] = converted_value
            yield keydict

    def __verify_model_class(self, csv_colnames: list[str], model_class: any) -> bool:
        model_obj = model_class()
        py_colnames = [csv_util.convert_colname(colname) for colname in csv_colnames]
        for colname in py_colnames:
            # ignore empty columns
            if colname == "":
                continue
            try:
                getattr(model_obj, colname)
            except AttributeError:
                print("key %s not found in %s" % (colname, model_class))
                return False
        return True
