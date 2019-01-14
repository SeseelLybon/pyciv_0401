
import pygame
pygame.init()


import generators
import time

import button
import scene

from buildings import buildings_dict
from buildings import BuildingTypes

from resources import resources_dict
from resources import ResourceTypes

print("Starting PyCiv 0401")


size = width, height = 600, 600

pos = [300, 300]

screen = pygame.display.set_mode(size)

mousex, mousey = 0, 0

black = 0, 0, 0


time_frame = 30  # frames
time_next = 0

scenes = {"Buildings": scene.Scene("Buildings List", (0, 110), (100, 0)),
          "Resources": scene.Scene("Resources List", (0, 110), (100, 0))}

scene_active = "Resources"

buttons = list()

buttons.append(button.Button("Buildings", ((0, 0), (300, 100)), 10, 10))
buttons.append(button.Button("Resources", ((300, 0), (300, 100)), 10, 10))


scenes["Buildings"].add_element("Smallstorage")
scenes["Buildings"].add_element("Small house")
scenes["Buildings"].add_element("Lumber camp")
scenes["Buildings"].add_element("Wood mill")
scenes["Buildings"].add_element("Quarry")
scenes["Buildings"].add_element("Stone cutters")

scenes["Resources"].add_element(resources_dict[ResourceTypes.people])
scenes["Resources"].add_element(resources_dict[ResourceTypes.stone])
scenes["Resources"].add_element(resources_dict[ResourceTypes.wood])

running = True


while running:
    time_next = time.time() + 1 / time_frame

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
            break

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                pass
            elif event.key == pygame.K_2:
                pass
            elif event.key == pygame.K_3:
                pass
            elif event.key == pygame.K_4:
                pass
        elif event.type == pygame.MOUSEMOTION:
            mousex, mousey = event.pos
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for thing in buttons:
                if thing.check_collision((mousex, mousey)):
                    if thing.text == "Buildings":
                        print("Activating scene", thing.text)
                        scene_active = "Buildings"
                    elif thing.text == "Resources":
                        print("Activating scene", thing.text)
                        scene_active = "Resources"

            for thing in scenes[scene_active].get_elements():
                if thing.check_collision((mousex, mousey)):
                    thing.do();

    # Do things here

    screen.fill((0, 0, 0))

    for thing in buttons:
        screen.blits(thing.blit())

    for thing in scenes.get(scene_active).blit():
        screen.blits(thing)

    pygame.display.flip()

    time_dif = time_next - time.time()
    if time_dif > 0:
        time.sleep(time_dif)


print("Reached end of main.py")

