import sys, pygame
import time
import math

from generator import generate_text_surface

print("Starting PyCiv 0401")

pygame.init()

size = width, height = 900, 600

pos = [300, 300]

screen = pygame.display.set_mode(size)


black = 0, 0, 0
time_frame = 30

time_next = 0

text_surface = []


text_surface[0] = generate_text_surface("")
text_surface[1] = generate_text_surface("")
text_surface[2] = generate_text_surface("")
text_surface[3] = generate_text_surface("")
text_surface[4] = generate_text_surface("")
text_surface[5] = generate_text_surface("")
text_surface[6] = generate_text_surface("")
text_surface[7] = generate_text_surface("")





running = True



while running:
    time_next = time.time() + 1 / time_frame

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
            break



        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                text_surface, rect = GAME_FONT.render("1 was pressed", (255, 255, 255))
            elif event.key == pygame.K_2:
                text_surface, rect = GAME_FONT.render("2 was pressed", (255, 255, 255))
            elif event.key == pygame.K_3:
                text_surface, rect = GAME_FONT.render("3 was pressed", (255, 255, 255))
            elif event.key == pygame.K_4:
                text_surface, rect = GAME_FONT.render("4 was pressed", (255, 255, 255))
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if get_collision() == True:
                text_surface, rect = GAME_FONT.render("Mouse was pressed", (255, 255, 255))

    #Do things here

    screen.fill(black)
    screen.blit(text_surface, (100, 100))
    pygame.display.flip()

    time_dif = time_next - time.time()
    if time_dif > 0:
        time.sleep(time_dif)
        # print("sleeping for:", time_dif)


print("Reached end of main.py")

