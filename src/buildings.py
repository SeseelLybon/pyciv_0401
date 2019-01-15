

from resources import ResourceTypes
from resources import resources_dict

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
    def __init__(self, typ, name, amount=0, produces=None, consumes=None, stores=None, costs=None, destruction=None):
        self.Type = typ
        self.Name = name
        self.Amount = amount

        if produces:
            self.Produces = produces
        else:
            self.Produces = dict()

        if consumes:
            self.Consumes = consumes
        else:
            self.Consumes = dict()

        if stores:
            self.Stores = stores
        else:
            self.Stores = dict()

        if costs:
            self.Costs = costs
        else:
            self.Costs = dict()

        if destruction:
            self.Destruction = destruction
        else:
            self.Destruction = dict()

    def add_building(self):
        # if resources are all available:
        self.Amount += 1
        # subtract resources

    def remove_building(self):
        # if resources are all available:
        if self.Amount > 0:
            self.Amount -= 1
        # add resources


buildings_dict = dict()

buildings_dict[BuildingTypes.Smallstorage] = Building(BuildingTypes.Smallstorage,
                                                      "Small storage",
                                                      amount=1,
                                                      stores={ResourceTypes.Wood : 1000}
                                                      )

buildings_dict[BuildingTypes.Smallhouse] = Building(BuildingTypes.Smallhouse,
                                                    "Small house",
                                                    amount=0,
                                                    stores={ResourceTypes.Wood : 1000}
                                                    )

buildings_dict[BuildingTypes.Lumbercamp] = Building(BuildingTypes.Lumbercamp,
                                                    "Lumber camp",
                                                    amount=0,
                                                    stores={ResourceTypes.Wood : 1000}
                                                    )

buildings_dict[BuildingTypes.Woodmill] = Building(BuildingTypes.Woodmill,
                                                  "Wood mill",
                                                  amount=0,
                                                  stores={ResourceTypes.Wood : 1000}
                                                  )

buildings_dict[BuildingTypes.Quarry] = Building(BuildingTypes.Quarry,
                                                "Quarry",
                                                amount=0,
                                                stores={ResourceTypes.Wood : 1000}
                                                )

buildings_dict[BuildingTypes.Stonecutters] = Building(BuildingTypes.Stonecutters,
                                                      "Stone cutters",
                                                      amount=0,
                                                      stores={ResourceTypes.Wood, 1000}
                                                      )





def Calculate_Produces(self):

    for key_r, value_r in resources_dict:
        gain = 0
        loss = 0

        for building in buildings_dict:
            loss -= building.Consumes[key_r]

        production = 0

        if value_r - loss <= 0:
            # precentage on how much is eventually produced
            production = 0
        else:
            resources_dict[key_r].Amount -= loss

        for building in buildings_dict:
            gain -= building.Produces[key_r]

        diffirence = gain - loss
