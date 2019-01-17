

import pygame
import generators
import math

from buildings import Building
from resources import Resource


image_button_add = pygame.image.load("../images/Button_Add.png")
image_button_remove = pygame.image.load("../images/Button_Remove.png")

class List_element:


    white = (200, 200, 200)
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
            self.image_button_add = image_button_add
            self.rect_button_add = pygame.Rect((0, 0), (0, 0))
            self.image_button_remove = image_button_remove
            self.rect_button_remove = pygame.Rect((0, 0), (0, 0))

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
        self.Text_surface_amount = generators.generate_text_surface(str(int(self.Thing.Amount)))

        if self.isBuilding:

            self.rect_button_add = pygame.Rect((0, 0), (0, 0))
            self.rect_button_remove = pygame.Rect((0, 0), (0, 0))

        else:

            self.rect_text_gain = pygame.Rect((0, 0), (0, 0))
            self.Text_surface_gain = generators.generate_text_surface(str(int(self.Thing.Produced)))

            self.rect_text_max = pygame.Rect((0, 0), (0, 0))
            self.Text_surface_max = generators.generate_text_surface("/"+str(int(self.Thing.Max)))

    def update_position(self, offset=(0, 0), outline_top=3, outline_sides=10, font_size=24):

        self.pos = offset

        self.rect = pygame.Rect((self.pos[0], self.pos[1]), self.size)
        self.rect_color = pygame.Surface(self.size)
        self.rect_color.fill(self.white)

        rect_inner_pos = (self.pos[0]+outline_sides,
                          self.pos[1]+outline_top)
        rect_inner_size = (self.size[0]-outline_sides*2,
                           self.size[1]-outline_top*2)

        self.rect_inner = pygame.Rect(rect_inner_pos, rect_inner_size)
        self.rect_inner_color = pygame.Surface(rect_inner_size)
        self.rect_inner_color.fill(self.black)

        text_outline_middle = (rect_inner_size[1]-font_size)//2+2

        rect_text_name_pos = (self.pos[0]+outline_sides*2,
                              self.pos[1]+outline_top+text_outline_middle)
        rect_text_name_size = (self.size[0]-outline_sides,
                               self.size[1]-outline_top-text_outline_middle)

        self.rect_text_name = pygame.Rect(rect_text_name_pos, rect_text_name_size)

        if self.isBuilding:

            rect_button_remove_pos = (self.pos[0] + outline_sides * 2 + 350,
                                      self.pos[1] + outline_top + text_outline_middle)
            rect_button_size = (20, 20)

            self.rect_button_remove = pygame.Rect(rect_button_remove_pos, rect_button_size)

            rect_text_amount_pos = (self.pos[0] + outline_sides * 2 + 400,
                                    self.pos[1] + outline_top + text_outline_middle)
            rect_text_amount_size = (self.size[0] - outline_sides,
                                     self.size[1] - outline_top - text_outline_middle)

            self.rect_text_amount = pygame.Rect(rect_text_amount_pos, rect_text_amount_size)
            self.Text_surface_amount = generators.generate_text_surface(str(int(self.Thing.Amount)))

            rect_button_add_pos = (self.pos[0] + outline_sides * 2 + 500,
                                   self.pos[1] + outline_top + text_outline_middle)

            self.rect_button_add = pygame.Rect(rect_button_add_pos, rect_button_size)
        else:

            rect_text_gain_pos = (self.pos[0] + outline_sides * 2 + 200,
                                  self.pos[1] + outline_top + text_outline_middle)
            rect_text_gain_size = (self.size[0] - outline_sides,
                                   self.size[1] - outline_top - text_outline_middle)

            self.rect_text_gain = pygame.Rect(rect_text_gain_pos, rect_text_gain_size)
            self.Text_surface_gain = generators.generate_text_surface(str(round(self.Thing.Produced, 4)))

            rect_text_amount_pos = (self.pos[0] + outline_sides * 2 + 300,
                                    self.pos[1] + outline_top + text_outline_middle)
            rect_text_amount_size = (self.size[0] - outline_sides,
                                     self.size[1] - outline_top - text_outline_middle)

            self.rect_text_amount = pygame.Rect(rect_text_amount_pos, rect_text_amount_size)
            self.Text_surface_amount = generators.generate_text_surface(str(int(self.Thing.Amount)))

            rect_text_max_pos = (self.pos[0] + outline_sides * 2 + 400,
                                 self.pos[1] + outline_top + text_outline_middle)
            rect_text_max_size = (self.size[0] - outline_sides,
                                  self.size[1] - outline_top - text_outline_middle)

            self.rect_text_max = pygame.Rect(rect_text_max_pos, rect_text_max_size)
            self.Text_surface_max = generators.generate_text_surface(("/"+str(self.Thing.Max)))

    def check_collision(self, pos):
        if self.isBuilding:
            if self.rect_button_add.collidepoint(pos):
                print("Pressed", self.Thing.Name, "Add")
                self.Thing.add_building()
            elif self.rect_button_remove.collidepoint(pos):
                print("Pressed", self.Thing.Name, "Remove")
                self.Thing.remove_building()

    def blit(self, offset):
        self.update_position(offset)

        if self.isBuilding:
            return [(self.rect_color, self.rect),
                    (self.rect_inner_color, self.rect_inner),
                    (self.Text_surface_name, self.rect_text_name),
                    (self.image_button_remove, self.rect_button_remove),
                    (self.Text_surface_amount, self.rect_text_amount),
                    (self.image_button_add, self.rect_button_add)
                    ]
        else:
            return [(self.rect_color, self.rect),
                    (self.rect_inner_color, self.rect_inner),
                    (self.Text_surface_name, self.rect_text_name),
                    (self.Text_surface_gain, self.rect_text_gain),
                    (self.Text_surface_amount, self.rect_text_amount),
                    (self.Text_surface_max, self.rect_text_max)
                    ]

    def do(self, args=None):
        print("Did click on", self.Thing.Name, self.Thing.Amount)
