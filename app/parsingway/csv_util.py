import re
from camel_converter import to_snake


def convert_colname(csvname: str) -> str:
    """Converts the name of a column in a csv file to a valid python variable name."""
    if csvname == "#":
        return "id"
    else:
        # Remove invalid characters
        fixed_name = re.sub('[^0-9a-zA-Z_]', '', csvname)
        # Remove leading characters until we find a letter or underscore
        fixed_name = re.sub('^[^a-zA-Z_]+', '', fixed_name)
        return to_snake(fixed_name)


def convert_value(python_datatype: str, value: str) -> int | bool | str:
    """Converts a string to the proper datatype. Accepts names converted by convert_datatype()."""
    if python_datatype == "int" or python_datatype == "FOREIGN_KEY":
        value = value.replace(".", "")  # For some reason some IDs are decimal numbers. Remove the dot, should still be unique.
        return int(value)
    elif python_datatype == "bool":
        return value.lower() == "true" or value == "1"
    elif python_datatype == "str":
        return value
    elif python_datatype == "float":
        return float(value)
    else:
        return None


def convert_datatype(csv_datatype: str) -> str:
    """Converts a datatype from the csv file to a valid python datatype.
    If the datatype is not recognized, it is assumed to be a foreign key, and return \"FOREIGN_KEY\"."""
    int_like = ["byte", "uint16", "uint32", "uint64", "int16", "int32", "int", "sbyte", "ubyte"]
    bool_like = ["bool"]
    # TODO int64 is supposed to be a integer, but the formatting in the csv file is strange.
    str_like = ["str", "Image", "Row", "Color", "int64"]  # TODO: fix Image, Row, Color
    float_like = ["single"]

    # special cases
    if csv_datatype.startswith("bit&"):
        return "bool"
    # list-based
    elif csv_datatype in int_like:
        return "int"
    elif csv_datatype in bool_like:
        return "bool"
    elif csv_datatype in str_like:
        return "str"
    elif csv_datatype in float_like:
        return "float"
    # Not in list -> probybly a reference to another table -> int
    else:
        return "FOREIGN_KEY"


def to_table_name(name: str) -> str:
    """Converts a string to a valid table name. A Table name is always in snake_case."""
    return to_snake(name)
