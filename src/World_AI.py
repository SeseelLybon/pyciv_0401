

from buildings import BuildingTypes
from buildings import buildings_dict

from resources import ResourceTypes
from resources import resources_dict


def live():
    if resources_dict[ResourceTypes.Troubles].Amount >= 10:
        resources_dict[ResourceTypes.AI_Build_Token].Amount += 1
        buildings_dict[BuildingTypes.Smallbanditcamp].add_building()









