from graphics import graphics
from menu import Menu
from shapely import geometry


class Nation:
    def __init__(self, name, position, color, soldiers, coords):
        self.name = name
        self.position = position
        self.color = color
        self.money = 100
        self.soldiers = soldiers

        self.points = coords

        self.shape = geometry.Polygon(shell=self.points)

        p1 = graphics.Point(self.position[0], self.position[1])
        p2 = graphics.Point(self.position[0] + 100, self.position[1] + 100)

        newPoints = []

        for point in self.points:
            newPoints.append(graphics.Point(point.x, point.y))

        self.rect = graphics.Polygon(newPoints)
        self.rect.setFill(self.color)
        self.rect.setOutline("black")


        center = graphics.Point(self.shape.centroid.coords.xy[0].pop(), self.shape.centroid.coords.xy[1].pop())

        self.mapText = graphics.Text(center, self.name + " - " + str(self.soldiers))



    def draw(self, window):
        self.rect.undraw()
        self.rect.draw(window)

        self.mapText.undraw()
        self.mapText.setText(self.name + " - " + str(self.soldiers))
        self.mapText.draw(window)
