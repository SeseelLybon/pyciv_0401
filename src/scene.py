import list_element


class Scene:

    def __init__(self, name, pos, size):
        self.name = name
        self.position = pos
        self.size = size
        self.container = list()

    def get_elements(self):
        return self.container

    def add_element(self, text):
        self.container.append(list_element.List_element(
            text
        ))

    def blit(self):
        temp = list()
        offset = [0, 0]
        for element in self.container:
            if element.isVisible:
                temp.append(element.blit((self.position[0], self.position[1]+offset[1])))
                offset[1] += 38
        return temp
