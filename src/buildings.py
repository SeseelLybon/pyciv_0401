

from resources import ResourceTypes
from resources import resources_dict

from enum import Enum
from enum import auto

import math

class BuildingTypes(Enum):
    Smallstorage = auto()
    Smallhouse = auto()
    Lumbercamp = auto()
    Woodmill = auto()
    Quarry = auto()
    Stonecutters = auto()
    Huntershut = auto()



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
        can_build = True
        for key_r, value_r in self.Costs.items():
            if resources_dict[key_r].Amount - value_r < 0:
                can_build = False

        if can_build:
            for key_r, value_r in self.Costs.items():
                resources_dict[key_r].Amount -= value_r
            self.Amount += 1
        # subtract resources

    def remove_building(self):
        # if resources are all available:
        if self.Amount > 0:
            self.Amount -= 1
            for key_r, value_r in self.Destruction.items():
                resources_dict[key_r].Amount += value_r
        # add resources

    def produce(self):
        amount_produced = self.Amount

        for key_r, value_r in self.Consumes.items():
            # Calc maximum amount of buildings that can produce
            a_min = resources_dict[key_r].Amount // value_r
            amount_produced = min(amount_produced, a_min)

        for key_r, value_r in self.Produces.items():
            # Calc maximum amount of buildings that can add to produced storage
            a_max = (resources_dict[key_r].Max - resources_dict[key_r].Amount) / value_r
            amount_produced = min(amount_produced, a_max)

        for key_r, value_r in self.Consumes.items():
            resources_dict[key_r].Amount -= value_r * amount_produced
            resources_dict[key_r].Produced -= value_r * amount_produced

        for key_r, value_r in self.Produces.items():
            resources_dict[key_r].Amount += value_r * amount_produced
            resources_dict[key_r].Produced += value_r * amount_produced
        return


def calc_max():

    for key_r, value_r in resources_dict.items():
        resources_dict[key_r].Max = 0
        resources_dict[key_r].Produced = 0

    for key_b, value_b in buildings_dict.items():
        for key_r, value_s in value_b.Stores.items():
            resources_dict[key_r].Max += value_s*value_b.Amount

    for key_r, value_r in resources_dict.items():
        resources_dict[key_r].Amount = min(resources_dict[key_r].Amount, resources_dict[key_r].Max)




buildings_dict = dict()

buildings_dict[BuildingTypes.Smallstorage] = Building(BuildingTypes.Smallstorage,
                                                      "Small storage",
                                                      amount=1,
                                                      costs={ResourceTypes.Wood: 100,
                                                             ResourceTypes.Stone: 100,
                                                             ResourceTypes.People: 1
                                                             },
                                                      stores={ResourceTypes.Logs: 1000,
                                                              ResourceTypes.Wood: 1000,
                                                              ResourceTypes.Stone: 1000,
                                                              ResourceTypes.Brick: 1000,
                                                              ResourceTypes.Food: 100
                                                              }
                                                      )

buildings_dict[BuildingTypes.Smallhouse] = Building(BuildingTypes.Smallhouse,
                                                    "Small house",
                                                    amount=1,
                                                    costs={ResourceTypes.Wood: 100,
                                                           ResourceTypes.Stone: 100,
                                                           ResourceTypes.People: 1
                                                           },
                                                    stores={ResourceTypes.People: 5
                                                            },
                                                    consumes={ResourceTypes.Food: 10
                                                              },
                                                    produces={ResourceTypes.People: 0.1
                                                              },
                                                    )

buildings_dict[BuildingTypes.Lumbercamp] = Building(BuildingTypes.Lumbercamp,
                                                    "Lumber camp",
                                                    amount=0,
                                                    costs={ResourceTypes.Wood: 100,
                                                           ResourceTypes.Stone: 100,
                                                           ResourceTypes.People: 1
                                                           },
                                                    produces={ResourceTypes.Logs: 10
                                                              },
                                                    destruction={ResourceTypes.Wood: 50,
                                                                 ResourceTypes.Stone: 50,
                                                                 ResourceTypes.People: 1
                                                                 }
                                                    )

buildings_dict[BuildingTypes.Woodmill] = Building(BuildingTypes.Woodmill,
                                                  "Wood mill",
                                                  amount=0,
                                                  costs={ResourceTypes.Wood: 100,
                                                         ResourceTypes.Stone: 100,
                                                         ResourceTypes.People: 1
                                                         },
                                                  consumes={ResourceTypes.Logs: 10
                                                            },
                                                  produces={ResourceTypes.Wood: 10
                                                            },
                                                  destruction={ResourceTypes.Wood: 50,
                                                               ResourceTypes.Stone: 50,
                                                               ResourceTypes.People: 1
                                                               }
                                                  )

buildings_dict[BuildingTypes.Quarry] = Building(BuildingTypes.Quarry,
                                                "Quarry",
                                                amount=0,
                                                costs={ResourceTypes.Wood: 100,
                                                       ResourceTypes.Stone: 100,
                                                       ResourceTypes.People: 1
                                                       },
                                                produces={ResourceTypes.Stone: 10
                                                          },
                                                destruction={ResourceTypes.Wood: 50,
                                                             ResourceTypes.Stone: 50,
                                                             ResourceTypes.People: 1
                                                             }
                                                )

buildings_dict[BuildingTypes.Stonecutters] = Building(BuildingTypes.Stonecutters,
                                                      "Stone cutters",
                                                      amount=0,
                                                      costs={ResourceTypes.Wood: 100,
                                                             ResourceTypes.Stone: 100,
                                                             ResourceTypes.People: 1
                                                             },
                                                      consumes={ResourceTypes.Stone: 10
                                                                },
                                                      produces={ResourceTypes.Brick: 10
                                                                },
                                                      destruction={ResourceTypes.Wood: 50,
                                                                   ResourceTypes.Stone: 50,
                                                                   ResourceTypes.People: 1
                                                                   }
                                                      )

buildings_dict[BuildingTypes.Huntershut] = Building(BuildingTypes.Huntershut,
                                                    "Hunter's hut",
                                                    amount=0,
                                                    costs={ResourceTypes.Wood: 100,
                                                           ResourceTypes.Stone: 100,
                                                           ResourceTypes.People: 1
                                                           },
                                                    produces={ResourceTypes.Food: 10
                                                              },
                                                    destruction={ResourceTypes.Wood: 50,
                                                                 ResourceTypes.Stone: 50,
                                                                 ResourceTypes.People: 1
                                                                 }
                                                    )






