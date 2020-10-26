from ShapeToGraphics import Shape
from graphics import graphics
from nation import Nation


class Region:

    def __init__(self, points, owner: Nation):
        self.shape = Shape.Shape(points)
        self.owner = owner

        newPoints = []
        for point in self.shape.points:
            newPoints.append(graphics.Point(point.x, point.y))

        center = graphics.Point(self.shape.polygon.centroid.coords.xy[0].pop(), self.shape.polygon.centroid.coords.xy[1].pop())

        self.mapText = graphics.Text(center, self.owner.name + " - " + str(self.owner.soldiers))

    def draw(self, window):
        self.shape.draw(window)

        self.mapText.undraw()
        self.mapText.setText(self.owner.name + " - " + str(self.owner.soldiers))
        self.mapText.draw(window)