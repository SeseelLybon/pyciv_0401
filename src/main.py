import pygame
import time
import math
import pygame.freetype

print("Hello world")

pygame.init()

size = width, height = 900, 600

pos = [300, 300]

screen = pygame.display.set_mode(size)


GAME_FONT = pygame.freetype.SysFont("Arial",24)
text_surface1, rect = GAME_FONT.render("Hello World!", (255, 255, 255))
text_surface2, rect = GAME_FONT.render("Hello World!", (255, 255, 255))
text_surface3, rect = GAME_FONT.render("Hello World!", (255, 255, 255))


black = 0, 0, 0
time_frame = 30

time_next = 0


running = True

while running:
    time_next = time.time() + 1 / time_frame

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
            break


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                text_surface, rect = GAME_FONT.render("1111111111", (255, 255, 255))
            if event.key == pygame.K_2:
                text_surface, rect = GAME_FONT.render("222222222", (255, 255, 255))
            if event.key == pygame.K_3:
                text_surface, rect = GAME_FONT.render("333333333", (255, 255, 255))
            if event.key == pygame.K_4:
                text_surface, rect = GAME_FONT.render("44444444444", (255, 255, 255))

    #Do things here

    screen.fill(black)
    screen.blit(text_surface1, (100, 100))
    screen.blit(text_surface2, (100, 200))
    screen.blit(text_surface3, (100, 300))
    pygame.display.flip()

    time_dif = time_next - time.time()
    if time_dif > 0:
        time.sleep(time_dif)
        # print("sleeping for:", time_dif)




print("Reached end of main.py")

