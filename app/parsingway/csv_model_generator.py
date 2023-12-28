import os
import json
from ..storingway import models
from . import csv_util


class CSVModelGenerator():

    def __init__(self, model_name: str, csv_colnames: list[str], csv_datatypes: list[str]):
        self.model_name = model_name
        self.table_name = csv_util.to_table_name(self.model_name)
        self.csv_colnames = csv_colnames
        self.csv_datatypes = csv_datatypes
        self.numAddedToParsingwayJson = 0

    def generate(self):
        model_fileds = ""
        schema_fields = ""
        constructor_fields = ""
        import_list = []

        # Process each column, resulting in one field per column
        for i in range(len(self.csv_colnames)):
            csv_colname = self.csv_colnames[i]
            csv_datatype = self.csv_datatypes[i]

            # Generate fields for this column
            (model_field, schema_field, constructor_field, foreign_model) = self.__generate_column(csv_colname, csv_datatype)
            model_fileds += model_field
            schema_fields += schema_field
            constructor_fields += constructor_field
            if foreign_model != "" and foreign_model not in import_list and foreign_model != self.model_name:
                import_list.append(foreign_model)
                # If the foreign model does not exist, add it to parsingway.json
                if not self.__model_file_exists(foreign_model):
                    self.__add_to_parsingway_json(foreign_model)

        generated_code = self.__generate_model_code(model_fileds, schema_fields, constructor_fields, import_list)
        self.__save_generated_code(generated_code)

    def __generate_column(self, csv_colname: str, csv_datatype: str):
        py_colname = csv_util.convert_colname(csv_colname)
        py_datatype = csv_util.convert_datatype(csv_datatype)
        model_field = ""
        schema_field = ""
        foreign_model = ""
        constructor_field = ""

        # Handle special cases
        if (py_colname == "id"):
            model_field = f"    {py_colname}: Mapped[int] = mapped_column(primary_key=True, index=True)\n"
            schema_field = f"        {py_colname}: int\n"
        # Ignore columns without a name, since we can't reference them in code.
        elif (py_colname == ""):
            pass
        # Handle primitive types
        elif (py_datatype == "int"):
            model_field = f"    {py_colname}: Mapped[int] = mapped_column()\n"
            schema_field = f"        {py_colname}: int\n"
        elif (py_datatype == "bool"):
            model_field = f"    {py_colname}: Mapped[bool] = mapped_column()\n"
            schema_field = f"        {py_colname}: bool\n"
        elif (py_datatype == "str"):
            model_field = f"    {py_colname}: Mapped[str] = mapped_column()\n"
            schema_field = f"        {py_colname}: str\n"
        elif (py_datatype == "float"):
            model_field = f"    {py_colname}: Mapped[float] = mapped_column()\n"
            schema_field = f"        {py_colname}: float\n"
        # Handle foreign keys
        elif (py_datatype == "FOREIGN_KEY"):
            foreign_table = csv_util.to_table_name(csv_datatype)
            foreign_model = csv_datatype
            model_field = f"    {py_colname}: Mapped[int] = mapped_column(ForeignKey(\"{foreign_table}.id\"))\n" +\
                          f"    {py_colname}_obj: Mapped\n"
            constructor_field = f"        self.{py_colname}_obj = relationship(\"{foreign_model}\", foreign_keys=[self.{py_colname}])\n"
            schema_field = f"        {foreign_table}: {foreign_model}.Schema\n"

        return (model_field, schema_field, constructor_field, foreign_model)

    def __model_file_exists(self, model_name: str) -> bool:
        """Checks if a file named model_name.py exists in the models folder."""
        return os.path.exists(os.path.join(models.__path__[0], model_name + ".py"))

    def __add_to_parsingway_json(self, model_name: str):
        """Adds a model_name to parsingway.json for it to be loaded the next time."""
        with open("resources/parsingway.json", "r+") as f:
            jsonfile = json.load(f)
            lst: list = jsonfile["csvparser"]
            datatype_str = f"{model_name}.csv"
            # Don't add duplicates
            if datatype_str not in lst:
                print(f"Model class {model_name} does not exist.")
                print(f"Adding {model_name}.csv to parsingway.json.")
                print("WARNING: PLEASE RESTART PROGRAM TO LOAD NEW PARSINGWAY.JSON")
                lst.append(datatype_str)
                jsonfile["csvparser"] = lst
                f.seek(0)
                json.dump(jsonfile, f, indent=4)
                f.truncate()
                self.numAddedToParsingwayJson += 1

    # TODO add Schema back in
    def __generate_model_code(self, model_fileds: str, schema_fields: str, constructor_fields: str, import_list: list[str]):
        # First some final post-processing
        import_string = "\n".join(
            # [f"    import app.storingway.models.{datatype} as {datatype}" for datatype in import_list])
            [f"    from app.storingway.models.{datatype} import {datatype}" for datatype in import_list])
        # This is the first actually working fix for the circular import problem.
        if import_string != "":
            import_string = f'''
from typing import TYPE_CHECKING
if TYPE_CHECKING:
{import_string}
'''

        # Actual code template
        generated_code = f'''from __future__ import annotations
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from pydantic import BaseModel
from .. import TableBase
{import_string}

class {self.model_name}(TableBase):
    __tablename__ = "{self.table_name}"
    __allow_unmapped__ = True
{model_fileds}
    def __init__(self, **kwargs):
{constructor_fields}
        super().__init__(**kwargs)

    class Schema(BaseModel):
{schema_fields}'''
        # class Schema(BaseModel):
        # {schema_fields}
        return generated_code

    def __save_generated_code(self, generated_code: str):
        new_filename = os.path.join(models.__path__[0], self.model_name + ".py")
        with open(new_filename, "w") as f:
            f.write(generated_code)
