import list_element


class Scene:

    elements = list()

    name = ""
    position = None
    size = None

    def __init__(self, name, pos, size):
        self.name = name
        self.position = pos
        self.size = size

    def get_elements(self):
        return self.elements

    def add_element(self, text):
        self.elements.append(list_element.List_element(
            text
        ))

    def blit(self):
        temp = list()
        offset = 0
        for i in self.elements:
            temp.append(i.blit((self.position[0],self.position[1]+offset)))
            offset += 50
        return temp
