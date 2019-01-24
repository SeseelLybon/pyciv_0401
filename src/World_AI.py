

from buildings import BuildingTypes
from buildings import buildings_dict

from resources import ResourceTypes
from resources import resources_dict

has_reached_coin = False


def live():
    global has_reached_coin

    try:
        # Small bandit camp spawn
        if has_reached_coin and resources_dict[ResourceTypes.Troubles].Amount >= 10:
            resources_dict[ResourceTypes.AI_Build_Token].Amount += 1
            buildings_dict[BuildingTypes.Smallbanditcamp].add_building()
            buildings_dict[BuildingTypes.Smallbanditcamp].isVisible = True
        if not has_reached_coin and buildings_dict[BuildingTypes.Coppermint].Amount >= 1:
            has_reached_coin = True

    except KeyError as ke:
        raise KeyError(ke, "Something went wrong in World_AI.",
                           "Note that World_AI is custom and has to be manually written.",
                           __file__)








