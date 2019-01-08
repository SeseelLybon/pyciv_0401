import list_element


class Scene:

    container = []

    name = ""
    position = None
    size = None

    def __init__(self, name, pos, size):
        self.name = name
        self.position = pos
        self.size = size

    def get_elements(self):
        return self.container

    def add_element(self, text):
        self.container.append(list_element.List_element(
            text, (0, 50*len(self.container))
        ))


    def blit(self):
        temp = list()
        for element in self.container:
            if element.isVisible:
                temp.append(element.blit((self.position[0],self.position[1])))
        return temp
