
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
            savable[value_r.Name] = [value_r.Amount, value_r.isVisible]
    elif BuildingTypes.Smallstorage in converter:
        for key_r, value_r in converter.items():
            savable[value_r.Name] = [value_r.Amount, value_r.isVisible]
    return savable


def generate_saveable_dicts():
    return {"Resources": generate_saveable_dict(resources_dict),
            "Buildings": generate_saveable_dict(buildings_dict)
            }


def generate_savefile():
    if not os.path.exists('../saves'):
        os.makedirs('../saves')

    with open("../saves/savefile.txt.tmp", "w") as f:
        f.write(json.dumps(generate_saveable_dicts(),
                           sort_keys=True, indent=4, separators=(',', ': ')))

    if os.path.exists('../saves/savefile.txt'):
        os.remove('../saves/savefile.txt')

    os.rename('../saves/savefile.txt.tmp', '../saves/savefile.txt')


def load_savefile():
    pass


