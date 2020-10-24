
from graphics import graphics
from shapely import geometry

from nation import Nation

size = (1000, 1000)
window = graphics.GraphWin("Map", size[0], size[1])
window.setCoords(0, 0, 500, 500)
nations = []
points = []
graphics_points = []

rect = graphics.Rectangle(graphics.Point(0, 400), graphics.Point(200, 500))
rect.setFill("grey")
rect.draw(window)

previous_point = None

name_box = graphics.Entry(rect.getCenter(), 10)
name_box.draw(window)

color_box = graphics.Entry(rect.getCenter(), 10)
color_box.move(0, -30)
color_box.draw(window)
while True:
    clickedPoint = window.getMouse()

    if 0 < clickedPoint.getX() < 200 and 400 < clickedPoint.getY() < 500:
        tempNation = Nation(name_box.getText(), color_box.getText(), 1000, points)

        f = open("nation_geometry.txt", "a")

        f.write(str(tempNation))
        print(str(tempNation))
        f.write("\n")
        f.close()
        graphics.Line(previous_point, graphics.Point(points[0].x, points[0].y)).draw(window)
        poly = graphics.Polygon(graphics_points)
        poly.setFill(color_box.getText())
        poly.draw(window)
        previous_point = None
        points = []
        graphics_points = []
        continue


    newPoint = geometry.Point(clickedPoint.getX(), clickedPoint.getY())
    points.append(newPoint)

    point = graphics.Point(clickedPoint.getX(), clickedPoint.getY()).draw(window)
    graphics_points.append(point)

    if previous_point is not None:
        graphics.Line(previous_point, clickedPoint).draw(window)
    previous_point = clickedPoint

