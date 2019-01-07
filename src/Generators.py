

import pygame.freetype

pygame.freetype.init()


def generate_text_surface(text, game_font = pygame.freetype.SysFont("Arial", 24)):
    text_surface, rect = game_font.render(text, (255, 255, 255))
    return text_surface

