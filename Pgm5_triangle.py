# triangle.py
# Jacob Manning
# Modified by Pharr to eliminate coordinates

from graphics import *

def Triangle():
    win_width = 400
    win_height = 400
    
    win = GraphWin("Draw a Triangle", win_width, win_height)
    message = Text(Point(win_width/2, win_height-10), "Click on three points")
    message.draw(win)

     # Get and draw three vertices of a triangle
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)

    # Get and draw triangle
    new_triangle = makeTriangle(p1, p2, p3)
    new_triangle.draw(win)

    # Math
    new_perimeter = perimeter(new_triangle)
    new_area = area(new_triangle)

    # Drawing math values in window
    perimeter_value = Text(Point(win_width/2, win_height-30), "Perimeter: "+str(new_perimeter))
    perimeter_value.draw(win)
    area_value = Text(Point(win_width/2, win_height-50), "Area: "+str(new_area))
    area_value.draw(win)

    # Wait for another click to exit
    message.setText("Click anywhere to quit")
    win.getMouse()
    win.close()

def makeTriangle(p1, p2, p3):

    # Use Polygon object to draw the triangle
    triangle = Polygon(p1, p2, p3)
    triangle.setFill("peachpuff")
    triangle.setOutline("cyan")
    return triangle

def distance(p1, p2):

    distX = (p1.getX() - p2.getX())**2
    distY = (p1.getY() - p2.getY())**2
    dist_total = (distX + distY)**.5
    return dist_total

def perimeter(tri):

    polygon_point_list = tri.getPoints()
    side_a = distance(polygon_point_list[0], polygon_point_list[1])
    side_b = distance(polygon_point_list[1], polygon_point_list[2])
    side_c = distance(polygon_point_list[2], polygon_point_list[0])
    perimeter = (side_a + side_b + side_c)/2
    return perimeter

def area(tri):

    polygon_point_list = tri.getPoints()
    side_a = distance(polygon_point_list[0], polygon_point_list[1])
    side_b = distance(polygon_point_list[1], polygon_point_list[2])
    side_c = distance(polygon_point_list[2], polygon_point_list[0])
    perimeter = (side_a + side_b + side_c)/2
    area = (perimeter*(perimeter - side_a)*(perimeter - side_b)*(perimeter - side_c))**.5
    return area

def main():
    Triangle()

main()
