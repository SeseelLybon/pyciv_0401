

from resources import ResourceTypes
from resources import resources_dict

from enum import Enum
import json
import os


class BuildingTypes(Enum):
    pass


'''
    Smallstorage = "Smallstorage"
    Smallhouse = "Smallhouse"
    Lumbercamp = "Lumbercamp"
    Woodmill = "Woodmill"
    Quarry = "Quarry"
    Huntershut = "Huntershut"
    Bank = "Bank"
    Smallloan = "Smallloan"
'''


class Building:
    def __init__(self, typ, name, amount=0, isvis=True,
                 produces=None,
                 consumes=None,
                 stores=None,
                 costs=None,
                 destruction=None):
        self.Type = typ
        self.Name = name
        self.Amount = amount
        self.isVisible = isvis

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
            if value_r > 0:
                if resources_dict[key_r].Amount - value_r < 0:
                    can_build = False
            elif value_r < 0:
                if resources_dict[key_r].Amount - value_r > resources_dict[key_r].Max:
                    can_build = False

        if can_build:
            for key_r, value_r in self.Costs.items():
                resources_dict[key_r].Amount -= value_r
            self.Amount += 1
        # subtract resources

    def remove_building(self):
        can_remove = True
        # if there are no buildings, no point in doing any of this
        if self.Amount > 0:
            # go through all the Destruction resources
            for key_r, value_r in self.Destruction.items():
                # if the value is below 0
                if value_r < 0:
                    # if the Amount of that resource drops below 0
                    if resources_dict[key_r].Amount + value_r < 0:
                        # can't remove the building
                        can_remove = False
        else:
            can_remove = False

        if can_remove:
            for key_r, value_r in self.Destruction.items():
                resources_dict[key_r].Amount += value_r
            self.Amount -= 1

    def produce(self):
        amount_produced = self.Amount

        # check if the buildings can consume enough resources
        for key_r, value_r in self.Consumes.items():
            # Calc maximum amount of buildings that can produce
            a_min = resources_dict[key_r].Amount // value_r
            amount_produced = min(amount_produced, a_min)

        amount_produced = abs(amount_produced)

        # check if the buildings aren't producing too much resources
        for key_r, value_r in self.Produces.items():
            # Calc maximum amount of buildings that can add to produced storage
            a_max = (resources_dict[key_r].Max - resources_dict[key_r].Amount) / value_r
            amount_produced = min(amount_produced, a_max)

        # actually consume resources
        for key_r, value_r in self.Consumes.items():
            resources_dict[key_r].Amount -= value_r * amount_produced
            resources_dict[key_r].Produced -= value_r * amount_produced

        # actually produce resources
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


def unpack_resources_dict(packed, building):
    produces = dict()
    consumes = dict()
    stores = dict()
    costs = dict()
    destruction = dict()

    for key_p, value_p in packed.items():
        try:
            if key_p == "produces":
                for key_, value_ in value_p.items():
                    typ = ResourceTypes[key_]
                    produces[typ] = value_

            elif key_p == "consumes":
                for key_, value_ in value_p.items():
                    typ = ResourceTypes[key_]
                    consumes[typ] = value_

            elif key_p == "stores":
                for key_, value_ in value_p.items():
                    typ = ResourceTypes[key_]
                    stores[typ] = value_

            elif key_p == "costs":
                for key_, value_ in value_p.items():
                    typ = ResourceTypes[key_]
                    costs[typ] = value_

            elif key_p == "destruction":
                for key_, value_ in value_p.items():
                    typ = ResourceTypes[key_]
                    destruction[typ] = value_
            else:
                raise ValueError("produces, consumes, stores, costs, destruction type failed",
                                 key_p, building)
        except KeyError as ke:
            raise KeyError(ke, building, "Couldn't find key", key_p, value_p)

    return produces, consumes, stores, costs, destruction


# (self, typ, name, amount=0, isvis=True, produces=None,consumes=None,stores=None,costs=None,destruction=None):

def generate_buildings_dict():
    global BuildingTypes
    bul_dict = dict()
    data_buildings = "data/buildings/"
    resources_folder = [f for f in os.listdir(data_buildings) if os.path.isfile(os.path.join(data_buildings, f))]
    loaded_buildings = dict()

    for file in resources_folder:
        try:
            with open(data_buildings+file, "r") as r:
                loaded_buildings.update(json.load(r))
        except json.decoder.JSONDecodeError as decoerr:
            raise TypeError(decoerr, data_buildings+file)

    buildings = []
    for key, value in loaded_buildings.items():
        buildings.append(value[0])

    BuildingTypes = Enum('BuildingTypes', buildings)

    for key, value in sorted(loaded_buildings.items()):
        typ = BuildingTypes[value[0]]
        produces, consumes, stores, costs, destruction = unpack_resources_dict(value[3], key)

        bul_dict[typ] = Building(typ, key, value[1], value[2],
                                 produces, consumes, stores, costs, destruction)

    return bul_dict


buildings_dict = generate_buildings_dict()

if __name__ == "__main__":
    for i in BuildingTypes:
        print(i)
