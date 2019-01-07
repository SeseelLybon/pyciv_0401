
import pygame
pygame.init()


import Generators
import time

import button
import scene

print("Starting PyCiv 0401")


size = width, height = 900, 600

pos = [300, 300]

screen = pygame.display.set_mode(size)

mousex, mousey = 0,0

black = 0, 0, 0


time_frame = 30
time_next = 0

scenes = dict()
scenes["Buildings"] = scene.Scene("Buildings List", (0, 300))
scenes["Resources"] = scene.Scene("Resources List", (0, 300))

scene_active = "Buildings"

buttons = list()

buttons.append(button.Button("Buildings", ((0, 0), (size[0]//2, 100)), 10, 10))
buttons.append(button.Button("Resources", ((size[0]//2, 0), (size[0]//2, 100)), 10, 10))


scenes["Buildings"].add_button("Headquarters")
scenes["Buildings"].add_button("Small house")
scenes["Buildings"].add_button("Lumber camp")
scenes["Buildings"].add_button("Wood mill")
scenes["Buildings"].add_button("Quarry")
scenes["Buildings"].add_button("Stone cutters")


scenes["Resources"].add_button(button.Button("People"))
scenes["Resources"].add_button(button.Button("Stone"))
scenes["Resources"].add_button(button.Button("Wood"))


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

    # Do things here

    screen.fill(black)

    for thing in buttons:
        screen.blits(thing.blit())

    for thing in scenes[scene_active]:
        screen.blits(thing.blit())

    pygame.display.flip()

    time_dif = time_next - time.time()
    if time_dif > 0:
        time.sleep(time_dif)
        # print("sleeping for:", time_dif)


print("Reached end of main.py")

