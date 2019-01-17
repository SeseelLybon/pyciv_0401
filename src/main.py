
import pygame
pygame.init()


import generators
import time

import button
import scene

from buildings import buildings_dict
from buildings import BuildingTypes
from buildings import calc_max

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


for key_b, value_b in buildings_dict.items():
    scenes["Buildings"].add_element(buildings_dict[key_b])

for key_r, value_r in resources_dict.items():
    scenes["Resources"].add_element(resources_dict[key_r])

running = True

frames_passed = 1

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
            if event.button == 1:
                for thing in buttons:
                    if thing.check_collision((mousex, mousey)):
                        if thing.text == "Buildings":
                            print("Activating scene", thing.text)
                            scene_active = "Buildings"
                        elif thing.text == "Resources":
                            print("Activating scene", thing.text)
                            scene_active = "Resources"

                for thing in scenes[scene_active].get_elements():
                    thing.check_collision((mousex, mousey))
            elif event.button == 4:
                # move the active scene up
                scenes.get(scene_active).move_scene((0, -20))
                pass
            elif event.button == 5:
                # move the active scene down
                scenes.get(scene_active).move_scene((0, 20))
                pass

    # Do things here

    frames_passed += 1
    if frames_passed % time_frame == 0:
        frames_passed = 0
        calc_max()

        for building in buildings_dict.values():
            building.produce()
            pass

    screen.fill((0, 0, 0))


    for thing in scenes.get(scene_active).blit():
        screen.blits(thing)

    for thing in buttons:
        screen.blits(thing.blit())

    pygame.display.flip()

    time_dif = time_next - time.time()
    if time_dif > 0:
        time.sleep(time_dif)


print("Reached end of main.py")

