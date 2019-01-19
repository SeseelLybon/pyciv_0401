

from enum import Enum
from enum import auto
import json


class ResourceTypes(Enum):
    pass


class Resource:
    def __init__(self, typ, name, amount, isvis=True):
        self.Type = typ
        self.Name = name
        self.Amount = amount
        self.Max = 0
        self.Produced = 0
        self.isVisible = isvis


def generate_resource_dict():
    global ResourceTypes
    res_dict = dict()

    with open("resources/resources.json", "r") as r:
        loaded_resources = json.load(r)

    resources = []
    for key, value in loaded_resources.items():
        resources.append(value[0])

    ResourceTypes = Enum('ResourceTypes', resources)

    for key, value in loaded_resources.items():
        # Brick ['ResourceTypes.Brick', 0, False]
        typ = ResourceTypes[value[0]]
        res_dict[typ] = Resource(typ, key, value[1], value[2])

    return res_dict


resources_dict = generate_resource_dict()

if __name__ == "__main__":
    for i in ResourceTypes:
        print(i)
