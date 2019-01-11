

from enum import Enum
from enum import auto


resources_dict = dict()


class ResourceTypes(Enum):
    wood = auto()
    stone = auto()
    people = auto()
    smallhouse = auto()
    lumbercamp = auto()
    quarry = auto()


resources_dict[ResourceTypes.wood] = 0
resources_dict[ResourceTypes.stone] = 0
resources_dict[ResourceTypes.people] = 0
