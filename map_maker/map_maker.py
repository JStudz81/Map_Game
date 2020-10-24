import nation
from graphics import graphics
from shapely import geometry

size = (1000, 1000)
window = graphics.GraphWin("Map", size[0], size[1])
window.setCoords(0, 0, 500, 500)
nations = []
points = []

rect = graphics.Rectangle(graphics.Point(0, 400), graphics.Point(200, 500))
rect.setFill("grey")
rect.draw(window)

previous_point = None
while True:
    clickedPoint = window.getMouse()

    if 0 < clickedPoint.getX() < 200 and 400 < clickedPoint.getY() < 500:
        f = open("nation_geometry.txt", "a")

        points.append(points[0])
        for point in points:
            f.write(str(point.x) + ":" + str(point.y) + ",")
            print(str(point.x) + " : " + str(point.y))
        f.write("\n")
        f.close()
        graphics.Line(previous_point, graphics.Point(points[0].x, points[0].y)).draw(window)
        previous_point = None
        points = []
        continue


    newPoint = geometry.Point(clickedPoint.getX(), clickedPoint.getY())
    points.append(newPoint)

    graphics.Point(clickedPoint.getX(), clickedPoint.getY()).draw(window)

    if previous_point is not None:
        graphics.Line(previous_point, clickedPoint).draw(window)
    previous_point = clickedPoint

