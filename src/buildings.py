

from resources import ResourceTypes

from enum import Enum
from enum import auto


class BuildingTypes(Enum):
    Smallstorage = auto()
    Smallhouse = auto()
    Lumbercamp = auto()
    Woodmill = auto()
    Quarry = auto()
    Stonecutters = auto()


class Building:
    def __init__(self, typ, name, amount=0, produces=None, consumes=None, stores=None,costs=None, destruction=None):
        self.Type = typ
        self.Name = name
        self.Amount = amount

        if produces:
            self.Produces = produces
        else:
            self.Produces = [(None, None)]

        if consumes:
            self.Consumes = consumes
        else:
            self.Consumes = [(None, None)]

        if stores:
            self.Stores = stores
        else:
            self.Stores = [(None, None)]

        if costs:
            self.Costs = costs
        else:
            self.Costs = [(None, None)]

        if destruction:
            self.Destruction = destruction
        else:
            self.Destruction = [(None, None)]

    def add_building(self):
        # if resources are all available:
        self.Amount += 1
        # subtract resources


buildings_dict = dict()

buildings_dict[BuildingTypes.Smallstorage] = Building(BuildingTypes.Smallstorage,
                                                      "Small storage",
                                                      amount=1,
                                                      stores=[(ResourceTypes.Wood, 1000)])

buildings_dict[BuildingTypes.Smallhouse] = Building(BuildingTypes.Smallhouse,
                                                    "Small house",
                                                    amount=0,
                                                    stores=[(ResourceTypes.Wood, 1000)])

buildings_dict[BuildingTypes.Lumbercamp] = Building(BuildingTypes.Lumbercamp,
                                                    "Lumber camp",
                                                    amount=0,
                                                    stores=[(ResourceTypes.Wood, 1000)])

buildings_dict[BuildingTypes.Woodmill] = Building(BuildingTypes.Woodmill,
                                                  "Wood mill",
                                                  amount=0,
                                                  stores=[(ResourceTypes.Wood, 1000)])

buildings_dict[BuildingTypes.Quarry] = Building(BuildingTypes.Quarry,
                                                "Quarry",
                                                amount=0,
                                                stores=[(ResourceTypes.Wood, 1000)])

buildings_dict[BuildingTypes.Stonecutters] = Building(BuildingTypes.Stonecutters,
                                                      "Stone cutters",
                                                      amount=0,
                                                      stores=[(ResourceTypes.Wood, 1000)])





