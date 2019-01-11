

import pygame
import generators


class List_element:

    text = ""
    white = (0, 0, 255)
    black = (0, 0, 0)
    isVisible = True

    def __init__(self, text, outline_top=3, outline_sides=10, font_size=24):
        self.container = []
        self.pos = (0, 0)
        self.size = (600, 40)

        self.text = text

        # Make white Rect
        self.rect = pygame.Rect(self.pos, self.size)
        self.rect_color = pygame.Surface(self.size)
        self.rect_color.fill(self.white)

        # Make a black rect inside the white Rect.
        self.rect_inner = pygame.Rect((0, 0), (0, 0))
        self.rect_inner_color = pygame.Surface((0, 0))
        self.rect_inner_color.fill(self.black)

        # Position the text surface inside the black Rect

        self.rect_text = pygame.Rect((0, 0), (0, 0))
        self.text_surface = generators.generate_text_surface(text)

    def update_position(self, offset=(0, 0), outline_top=3, outline_sides=10, font_size=24):
        self.text = text

        self.pos = offset

        self.rect = pygame.Rect((self.pos[0], self.pos[1]), self.size)
        self.rect_color = pygame.Surface(self.size)
        self.rect_color.fill(self.white)

        rect_inner_pos = (self.pos[0]+outline_sides, self.pos[1]+outline_top)
        rect_inner_size = (self.size[0]-outline_sides*2, self.size[1]-outline_top*2)

        self.rect_inner = pygame.Rect(rect_inner_pos, rect_inner_size)
        self.rect_inner_color = pygame.Surface(rect_inner_size)
        self.rect_inner_color.fill(self.black)

        text_outline_middle = (rect_inner_size[1]-font_size)//2+2

        rect_text_pos = (self.pos[0]+outline_sides*2, self.pos[1]+outline_top+text_outline_middle)
        rect_text_size = (self.size[0]-outline_sides, self.size[1]-outline_top-text_outline_middle)

        self.rect_text = pygame.Rect(rect_text_pos, rect_text_size)

    def check_collision(self, pos):
        if self.rect.collidepoint(pos):
            return True
        else:
            return False

    def blit(self, offset):
        self.update_position(offset)

        return [(self.rect_color, self.rect),
                (self.rect_inner_color, self.rect_inner),
                (self.text_surface, self.rect_text)
                ]

    def change_text(self, text):
        self.text = text
        self.text_surface = generators.generate_text_surface(self.text)

    def do(self, args=None):
        print("Did click on", self.text)
