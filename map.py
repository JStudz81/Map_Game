from graphics import graphics

class Map:
    def __init__(self):
        self.size = (1000, 1000)
        self.window = graphics.GraphWin("Map", self.size[0], self.size[1])
        self.window.setCoords(0, 0, 500, 500)
        self.nations = []

    def draw(self):
        for nation in self.nations:
            nation.draw(self.window)
