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
    if python_datatype == "int":
        return int(value)
    elif python_datatype == "bool":
        return value.lower() == "true" or value == "1"
    elif python_datatype == "str":
        return value
    elif python_datatype == "FOREIGN_KEY":
        return int(value)
    else:
        return None


def convert_datatype(csv_datatype: str) -> str:
    """Converts a datatype from the csv file to a valid python datatype.
    If the datatype is not recognized, it is assumed to be a foreign key, and return \"FOREIGN_KEY\"."""
    int_like = ["byte", "single", "uint16", "uint32", "uint64", "int16", "int32", "int64", "int", "sbyte", "ubyte"]
    bool_like = ["bool"]
    str_like = ["str", "Image", "Row", "Color"]  # TODO: fix Image, Row, Color

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
    # Not in list -> probybly a reference to another table -> int
    else:
        return "FOREIGN_KEY"


def to_table_name(name: str) -> str:
    """Converts a string to a valid table name. A Table name is always in snake_case."""
    return to_snake(name)
