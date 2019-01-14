

from enum import Enum
from enum import auto


resources_dict = dict()


class ResourceTypes(Enum):
    Wood = auto()
    Stone = auto()
    People = auto()


class Resource:
    def __init__(self, typ, name, amount):
        self.Type = typ
        self.Name = name
        self.Amount = amount


resources_dict[ResourceTypes.Wood] = 0
resources_dict[ResourceTypes.Stone] = 0
resources_dict[ResourceTypes.People] = 0
