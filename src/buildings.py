import resources

from enum import Enum
from enum import auto


class BuildingTypes(Enum):
    headquarters = auto()
    smallhouse = auto()
    lumbercamp = auto()
    woodmill = auto()
    quarry = auto()
    stonecutters = auto()


class SmallHouse:
    amount = 0
    produces = [(resources.ResourceTypes.people, 0.001)]
    consumes = [(None, None)]


class LumberCamp:
    amount = 0
    produces = [(resources.ResourceTypes.wood, 10)]
    consumes = [(None, None)]


class Quarry:
    amount = 0
    produces = [(resources.ResourceTypes.stone, 10)]
    consumes = [(None, None)]


buildings_dict = dict()

buildings_dict[BuildingTypes.headquarters] = 0
buildings_dict[BuildingTypes.smallhouse] = SmallHouse()
buildings_dict[BuildingTypes.lumbercamp] = LumberCamp()
buildings_dict[BuildingTypes.woodmill] = 0
buildings_dict[BuildingTypes.quarry] = Quarry()
buildings_dict[BuildingTypes.stonecutters] = 0





