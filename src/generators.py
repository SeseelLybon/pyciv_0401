
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
    path = "data/saves/"
    if not os.path.exists(path):
        os.makedirs(path)

    try:
        with open(path+"savefile.json.tmp", "w") as f:
            f.write(json.dumps(generate_saveable_dicts(),
                               sort_keys=True, indent=4, separators=(',', ': ')))
    except KeyError as ke:
        print(ke, "Couldn't find key in savefile", "At this time, manually delete")

    if os.path.exists(path+"savefile.json"):
        os.remove(path+"savefile.json")

    os.rename(path+"savefile.json.tmp", path+"savefile.json")


def load_savefile():
    path = "resources/saves"

    if os.path.exists(path+"savefile.json"):
        with open(path+"savefile.json", "r") as f:
            saved_object = json.load(f)
        for key, value in saved_object.items():
            if key == "Buildings":
                for key_, value_ in value.items():
                    try:
                        # Bank ['BuildingTypes.Bank', 0, True]
                        typ = BuildingTypes[value_[0]]
                        buildings_dict[typ].Amount = value_[1]
                        buildings_dict[typ].isVisible = value_[2]
                    except KeyError as ke:
                        raise KeyError(ke, "Couldn't find this building key", "manually remove or edit key",
                                           __file__)
            elif key == "Resources":
                for key_, value_ in value.items():
                    try:
                        # Brick ['ResourceTypes.Brick', 0, False]
                        typ = ResourceTypes[value_[0]]
                        resources_dict[typ].Amount = value_[1]
                        resources_dict[typ].isVisible = value_[2]
                    except KeyError as ke:
                        print(ke, "Couldn't find this resource key", "manually remove or edit key", key_, value_,
                                  __file__)

