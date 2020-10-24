from graphics import graphics
from menu import Menu
from shapely import geometry
import json


class Nation:
    def __init__(self, name, color, soldiers, coords=None, position=None):
        if coords is None:
            coords = []
        if position is None:
            position = [0, 0]
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

    def __str__(self):
        points = {}
        i = 0
        for point in self.points:
            points[i] = {"x": point.x, "y": point.y}
            i = i + 1
        return json.dumps({"name": self.name, "color": self.color, "points": points})
