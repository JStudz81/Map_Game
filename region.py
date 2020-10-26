from ShapeToGraphics import Shape
from graphics import graphics


class Region:

    def __init__(self, points):
        self.shape = Shape.Shape(points)
        self.name = "test"

        newPoints = []
        for point in self.shape.points:
            newPoints.append(graphics.Point(point.x, point.y))

        center = graphics.Point(self.shape.polygon.centroid.coords.xy[0].pop(), self.shape.polygon.centroid.coords.xy[1].pop())

        self.mapText = graphics.Text(center, self.name)

    def draw(self, window):
        self.shape.draw(window)

        self.mapText.undraw()
        self.mapText.setText(self.name)
        self.mapText.draw(window)