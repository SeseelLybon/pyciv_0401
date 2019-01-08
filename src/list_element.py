

import pygame
import generators


class List_element:

    text = ""
    white = (0, 0, 200)
    black = (0, 0, 0)
    container = []
    isVisible = True

    def __init__(self, text, pos, outline_top=10, outline_sides=10, font_size=24):
        self.container = []
        pos, size = pos, (300, 40)

        self.text = text

        self.rect = pygame.Rect(pos, size)
        self.rect_color = pygame.Surface(size)
        self.rect_color.fill(self.white)

        rect_inner_pos = (pos[0]+outline_top, pos[1]+outline_sides)
        rect_inner_size = (size[0]-outline_top*2, size[1]-outline_sides*2)

        self.rect_inner = pygame.Rect(rect_inner_pos, rect_inner_size)
        self.rect_inner_color = pygame.Surface(rect_inner_size)
        self.rect_inner_color.fill(self.black)

        text_outline_middle = (rect_inner_size[1]-font_size)//2

        rect_text_pos = (pos[0]+outline_top*2, pos[1]+outline_sides+text_outline_middle)
        rect_text_size = (size[0]-outline_top, size[1]-outline_sides-text_outline_middle)

        self.rect_text = pygame.Rect(rect_text_pos, rect_text_size)
        self.text_surface = generators.generate_text_surface(text)

    def check_collision(self, pos, offset=(0, 0)):
        if self.rect.collidepoint((pos[0]+offset[0], pos[1]+offset[1])):
            return True
        else:
            return False

    def blit(self, offset):
        return [(self.rect_color, self.rect.move(offset[0], offset[1])),
                (self.rect_inner_color, self.rect_inner.move(offset[0], offset[1])),
                (self.text_surface, self.rect_text.move(offset[0], offset[1]))
                ]

    def change_text(self, text):
        self.text = text
        self.text_surface = generators.generate_text_surface(self.text)

    def do(self, args=None):
        print("Did click on", self.text)
