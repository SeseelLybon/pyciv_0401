

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
        self.Max = amount
        self.Produced = 0


resources_dict[ResourceTypes.Wood] = Resource(ResourceTypes.Wood, "Wood", 1000)
resources_dict[ResourceTypes.Stone] = Resource(ResourceTypes.Stone, "Stone", 1000)
resources_dict[ResourceTypes.People] = Resource(ResourceTypes.People, "People", 10)
