import button


class Scene:

    elements = list()

    name = ""
    position = None

    def __init__(self, name, pos):
        self.name = name
        self.position = pos

    def get_elements(self):
        return self.elements

    def add_element(self, text):
        self.elements.append(button.Button(
            text, ((0, 0), (0, 0)), 10, 0
        ))

    def blit(self):
        return [i.blit() for i in self.elements]
