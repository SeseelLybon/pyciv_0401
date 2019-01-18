

from enum import Enum
from enum import auto


resources_dict = dict()


class ResourceTypes(Enum):
    Logs = "Logs"
    Wood = "Wood"
    Stone = "Stone"
    Brick = "Brick"
    People = "People"
    Food = "Food"
    Coin = "Coin"


class Resource:
    def __init__(self, typ, name, amount, isvis=True):
        self.Type = typ
        self.Name = name
        self.Amount = amount
        self.Max = 0
        self.Produced = 0
        self.isVisible = isvis


resources_dict[ResourceTypes.Logs] = Resource(ResourceTypes.Logs, "Logs", 0)
resources_dict[ResourceTypes.Wood] = Resource(ResourceTypes.Wood, "Wood", 1000)
resources_dict[ResourceTypes.Stone] = Resource(ResourceTypes.Stone, "Stone", 1000)
resources_dict[ResourceTypes.Brick] = Resource(ResourceTypes.Brick, "Brick", 0, False)
resources_dict[ResourceTypes.People] = Resource(ResourceTypes.People, "People", 10)
resources_dict[ResourceTypes.Food] = Resource(ResourceTypes.Food, "Food", 1000)
resources_dict[ResourceTypes.Coin] = Resource(ResourceTypes.Coin, "Coin", 0)
