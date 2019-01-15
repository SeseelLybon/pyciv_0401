

import pygame
import generators

from buildings import Building
from resources import Resource


class List_element:

    white = (0, 0, 255)
    black = (0, 0, 0)
    isVisible = True
    isBuilding = False  # if it is not a building, it is a resource

    # Rect Rect
    # Surface Rect_color

    # Rect Rect_inner
    # Surface Rect_inner_color

    # Rect Rect_text
    # Surface text_surface
    # String text = ""

    # Rect Rect_text_amount
    # Text_surface_amonut

    #
    # Building/Resource Thing = None # What does this lis_element represent?

    def __init__(self, objct, outline_top=3, outline_sides=10, font_size=24):

        self.Thing = objct
        if isinstance(self.Thing, Building):
            self.isBuilding = True
        elif isinstance(self.Thing, Resource):
            self.isBuilding = False

        self.container = []
        self.pos = (0, 0)
        self.size = (600, 40)

        # Make white Rect
        self.rect = pygame.Rect(self.pos, self.size)
        self.rect_color = pygame.Surface(self.size)
        self.rect_color.fill(self.white)

        # Make a black rect inside the white Rect.
        self.rect_inner = pygame.Rect((0, 0), (0, 0))
        self.rect_inner_color = pygame.Surface((0, 0))
        self.rect_inner_color.fill(self.black)

        # Position the text surface inside the black Rect

        self.rect_text_name = pygame.Rect((0, 0), (0, 0))
        self.Text_surface_name = generators.generate_text_surface(self.Thing.Name)

        self.rect_text_amount = pygame.Rect((0, 0), (0, 0))
        self.Text_surface_amount = generators.generate_text_surface(str(self.Thing.Amount))

    def update_position(self, offset=(0, 0), outline_top=3, outline_sides=10, font_size=24):

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

        rect_text_name_pos = (self.pos[0]+outline_sides*2, self.pos[1]+outline_top+text_outline_middle)
        rect_text_name_size = (self.size[0]-outline_sides, self.size[1]-outline_top-text_outline_middle)

        self.rect_text_name = pygame.Rect(rect_text_name_pos, rect_text_name_size)

        rect_text_amount_pos = (self.pos[0]+outline_sides*2+300, self.pos[1]+outline_top+text_outline_middle)
        rect_text_amount_size = (self.size[0]-outline_sides, self.size[1]-outline_top-text_outline_middle)

        self.rect_text_amount = pygame.Rect(rect_text_amount_pos, rect_text_amount_size)
        self.Text_surface_amount = generators.generate_text_surface(str(self.Thing.Amount))

    def check_collision(self, pos):
        if self.rect.collidepoint(pos):
            return True
        else:
            return False

    def blit(self, offset):
        self.update_position(offset)

        return [(self.rect_color, self.rect),
                (self.rect_inner_color, self.rect_inner),
                (self.Text_surface_name, self.rect_text_name),
                (self.Text_surface_amount, self.rect_text_amount)
                ]

    def do(self, args=None):
        print("Did click on", self.Thing.Name, self.Thing.Amount)
