from enum import Enum

from app.storingway.crud import crud_gathering

gathering_types_dict = {str(i.id): i.name for i in crud_gathering.get_gathering_types()}
gathering_types_dict.pop("4")  # Remove currently unused types
gathering_types_dict.pop("5")
GatheringTypes: Enum = Enum("GatheringTypes", gathering_types_dict)
