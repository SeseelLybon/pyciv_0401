

import pygame
import generators


class List_element:

    text = ""
    white = (0, 0, 200)
    black = (0, 0, 0)
    isVisible = True

    def __init__(self, text, outline_top=3, outline_sides=10, font_size=24):
        self.container = []
        self.pos = (0, 0)
        self.size =  (600, 40)

        self.text = text

        self.rect = pygame.Rect(self.pos, self.size)
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
        self.text_surface = generators.generate_text_surface(text)

    def update_position(self):
        pass

    def check_collision(self, pos, offset=(0, 0)):
        if self.rect.collidepoint((pos[0]+offset[0], pos[1]+offset[1])):
            return True
        else:
            return False

    def blit(self, offset):
        self.rect.y = offset[1]
        self.rect_inner.y = offset[1]
        self.rect_text.y = offset[1]

        return [(self.rect_color, self.rect),
                (self.rect_inner_color, self.rect_inner),
                (self.text_surface, self.rect_text)
                ]

    def change_text(self, text):
        self.text = text
        self.text_surface = generators.generate_text_surface(self.text)

    def do(self, args=None):
        print("Did click on", self.text)
