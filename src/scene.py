import list_element


class Scene:

    def __init__(self, name, pos, size):
        self.name = name
        self.position = pos
        self.top = self.position
        self.size = size
        self.container = list()

    def get_elements(self):
        return self.container

    def add_element(self, objct):
        self.container.append(list_element.List_element(
            objct
        ))

    def move_scene(self, offset):
        # If the offset is negative (scroll up)
        if offset[1] < 0:
            bottom = 0
            for element in self.container:
                if element.Thing.isVisible:
                    bottom += 30

            if self.position[1]+bottom+offset[1] >= self.top[1]+30*8:
                self.position = (self.position[0]+offset[0], self.position[1]+offset[1])

        # If the offset is positive (scroll down)
        elif offset[1] > 0:

            if self.position[1]+offset[1] <= self.top[1]:
                self.position = (self.position[0]+offset[0], self.position[1]+offset[1])

    def blit(self):
        temp = list()
        offset = [0, 0]
        for element in self.container:
            if element.Thing.isVisible:
                temp.append(element.blit((self.position[0], self.position[1]+offset[1])))
                offset[1] += 38
        return temp
