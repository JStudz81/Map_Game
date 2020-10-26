from graphics import graphics
from menu import Menu
from shapely import geometry
import json
from ShapeToGraphics import Shape


class Nation:
    def __init__(self, name, color, soldiers):
        self.name = name

        self.color = color
        self.money = 100
        self.soldiers: int = soldiers






    # def __str__(self):
    #     points = {}
    #     i = 0
    #     for point in self.points:
    #         points[i] = {"x": point.x, "y": point.y}
    #         i = i + 1
    #     return json.dumps({"name": self.name, "color": self.color, "points": points})
