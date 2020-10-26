from typing import List

from graphics import graphics
from menu import Menu
from shapely import geometry
import json
from ShapeToGraphics import Shape
from region import Region


class Nation:
    def __init__(self, name, color, soldiers):
        self.name = name

        self.color = color
        self.money = 100
        self.soldiers: int = soldiers
        self.regions: List[Region] = []

    def add_regions(self, regions: List[Region]):
        self.regions = self.regions + regions
        for region in regions:
            region.owner = self
            region.shape.color = self.color
            region.mapText.setText("")






    # def __str__(self):
    #     points = {}
    #     i = 0
    #     for point in self.points:
    #         points[i] = {"x": point.x, "y": point.y}
    #         i = i + 1
    #     return json.dumps({"name": self.name, "color": self.color, "points": points})
