from typing import List

from shapely import geometry
from graphics import graphics

class Shape:

    def __init__(self, points:List[geometry.Point]):
        self.points: List[geometry.Point] = points
        self.polygon: geometry.Polygon = geometry.Polygon(self.points)
        self.graphicsPoly = None
        self.color = "white"

    def to_graphics_points(self):
        graphics_points: List[graphics.Point] = []
        for point in self.points:
            graphics_points.append(graphics.Point(point.x, point.y))
        return graphics_points

    def draw(self, window):
        if self.graphicsPoly is None:
            self.graphicsPoly = graphics.Polygon(self.to_graphics_points())
        else:
            self.graphicsPoly.undraw()
        self.graphicsPoly.setFill(self.color)
        self.graphicsPoly.draw(window)

