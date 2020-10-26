from ShapeToGraphics.Shape import Shape
from graphics import graphics
from shapely import geometry

def shape_to_graphic(polygon: Shape):
     graphicPoly = graphics.Polygon(polygon.to_graphics_points())

