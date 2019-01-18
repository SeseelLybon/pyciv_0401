
import os
import pygame.freetype

from resources import resources_dict
from resources import ResourceTypes

from buildings import buildings_dict
from buildings import BuildingTypes

import json

pygame.freetype.init()


def generate_text_surface(text, game_font = pygame.freetype.SysFont("Arial", 24)):
    text_surface, rect = game_font.render(text, (255, 255, 255))
    return text_surface


def generate_saveable_dict(converter):
    savable = dict()
    if ResourceTypes.Logs in converter:
        for key_r, value_r in converter.items():
            savable[value_r.Name] = [str(value_r.Type).split('.')[1], value_r.Amount, value_r.isVisible]
    elif BuildingTypes.Smallstorage in converter:
        for key_r, value_r in converter.items():
            savable[value_r.Name] = [str(value_r.Type).split('.')[1], value_r.Amount, value_r.isVisible]
    return savable


def generate_saveable_dicts():
    return {"Resources": generate_saveable_dict(resources_dict),
            "Buildings": generate_saveable_dict(buildings_dict)
            }


def generate_savefile():
    if not os.path.exists('../saves'):
        os.makedirs('../saves')

    with open("../saves/savefile.json.tmp", "w") as f:
        f.write(json.dumps(generate_saveable_dicts(),
                           sort_keys=True, indent=4, separators=(',', ': ')))

    if os.path.exists('../saves/savefile.json'):
        os.remove('../saves/savefile.json')

    os.rename('../saves/savefile.json.tmp', '../saves/savefile.json')


def load_savefile():
    with open("../saves/savefile.json", "r") as f:
        saved_object = json.load(f)

    for key, value in saved_object.items():
        if key == "Buildings":
            for key_, value_ in value.items():
                # Bank ['BuildingTypes.Bank', 0, True]
                typ = BuildingTypes[value_[0]]
                buildings_dict[typ].Amount = value_[1]
                buildings_dict[typ].isVisible = value_[2]
        elif key == "Resources":
            for key_, value_ in value.items():
                # Brick ['ResourceTypes.Brick', 0, False]
                typ = ResourceTypes[value_[0]]
                resources_dict[typ].Amount = value_[1]
                resources_dict[typ].isVisible = value_[2]


if __name__ == "__main__":
    pass
