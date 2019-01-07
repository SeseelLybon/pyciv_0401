
import pygame.freetype




def generate_text_surface(text = "Hello World!", color = (255,255,255)):
    GAME_FONT = pygame.freetype.SysFont("Arial", 24)
    text_surface, rect = GAME_FONT.render(text, (pos))

    return text_surface
