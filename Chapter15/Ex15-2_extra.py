import math
import turtle

def draw_axes(t, length):
    """Uses turtle to draw x and y axes, returns turtle to (0,0), heading 0"""
    t.pd()
    t.setheading(90)
    t.fd(length)
    t.rt(180)
    t.fd(length * 2)
    t.goto(0,0)
    t.setheading(0)
    t.fd(length)
    t.rt(180)
    t.fd(length * 2)
    t.goto(0,0)
    t.setheading(0)
    
def draw_rect(t, rectangle):
    """Takes a Turtle and a Rectangle, uses the turtle to draw the rectangle"""
    t.pu()
    t.goto(rectangle.corner.x, rectangle.corner.y)
    t.setheading(0)
    t.pd()
    t.fd(rectangle.width)
    t.rt(90)
    t.fd(rectangle.height)
    t.rt(90)
    t.fd(rectangle.width)
    t.rt(90)
    t.fd(rectangle.height)
    t.pu()
    t.goto(0,0)
    t.setheading(0)


def draw_circle(t, circle):
    """Takes a Turtle and a Circle, uses the turtle to draw the circle"""
    t.pu()
    t.goto(circle.centre.x + circle.radius, circle.centre.y)
    t.setheading(90)
    t.pd()
    t.circle(circle.radius)
    t.pu()
    t.goto(0,0)
    t.setheading(0)

def point_in_circle(circle, point):
    """Takes a Circle object and a Point.
        Returns True if the Point lies within or on the boundary of the Circle
        """
    dx = abs(point.x - circle.centre.x)
    dy = abs(point.y - circle.centre.y)
    distance_point_to_centre = math.sqrt(dx**2 + dy**2)
    return distance_point_to_centre <= circle.radius

def rect_in_circle(circle, rectangle):
    """Takes a Circle and a Rectange, returns True if the rectangle lies
        entirely in or on the boundary of the Circle"""
    #find four corners of rectangle
    top_left = rectangle.corner
    top_right = create_moved_point(rectangle.corner, rectangle.corner.x + rectangle.width, 0)
    bottom_left = create_moved_point(rectangle.corner, 0 , rectangle.corner.y + rectangle.height)
    bottom_right = create_moved_point(rectangle.corner, rectangle.corner.x + rectangle.width,  rectangle.corner.y + rectangle.height)
    return point_in_circle(circle, top_left) and point_in_circle(circle, top_right) and point_in_circle(circle, bottom_left) and \
           point_in_circle(circle, bottom_right) 

def create_moved_point(point, dx, dy):
    """Takes a Point object, returns a new Point moved by dx and dy"""
    result = Point()
    result.x = point.x + dx
    result.y = point.y + dy
    return result

def rect_corners_and_circle_overlap(circle, rectangle):
    """Takes a Circle and Rectangle object, returns True if any of the rectangle corners falls inside the circle"""
    top_left = rectangle.corner
    top_right = create_moved_point(rectangle.corner, rectangle.corner.x + rectangle.width, 0)
    bottom_left = create_moved_point(rectangle.corner, 0 , rectangle.corner.y + rectangle.height)
    bottom_right = create_moved_point(rectangle.corner, rectangle.corner.x + rectangle.width,  rectangle.corner.y + rectangle.height)
    return point_in_circle(circle, top_left) or point_in_circle(circle, top_right) or point_in_circle(circle, bottom_left) or \
           point_in_circle(circle, bottom_right)     


def rect_inside_circle(circle, rectangle):
    """Takes a Circle and a Rectangle. Returns True if any part of the Rectangle falls inside the circle.
        Algorithm taken from:
        https://stackoverflow.com/questions/401847/circle-rectangle-collision-detection-intersection"""
    
    rectangle.centre = find_centre(rectangle)
    dx = abs(circle.centre.x - rectangle.centre.x)#x difference between centre of circle and rectangle
    dy = abs(circle.centre.y - rectangle.centre.y) #y difference between centre of circle and rectangle

    if dx > (rectangle.width/2 + circle.radius):
        return False
    if dy > (rectangle.height/2 + circle.radius):
        return False

    if dx <= (rectangle.width/2):
        return True
    if dy <= (rectangle.height/2):
        return True

    corner_distance_squared = (dx - rectangle.width/2)**2 + (dy - rectangle.height/2)**2
    return corner_distance_squared <= (circle.radius**2)
    
    
def find_centre(rect):
    rect_centre = Point()
    rect_centre.x = rect.corner.x + rect.width/2
    rect_centre.y = rect.corner.y - rect.height/2
    return rect_centre


class Point:
    """Represents a point in 2D space"""

class Circle:
    """Represents a circle.
        attributes:
        centre (a Point object)
        radius (a number)"""

class Rectangle:
    """ Represents a rectangle with sides parallel to x or y axes
        Attributes:
        corner - Point object locating top left corner of rectange
        width
        height
        """
        
def main():
    circ = Circle()
    circ.centre = Point()
    circ.centre.x = -25
    circ.centre.y = 20
    circ.radius = 50.0

    point = Point()
    point.x = 0
    point.y = 0

    rect = Rectangle()
    rect.corner = Point()
    rect.corner.x = 30
    rect.corner.y = 20
    rect.width = 50.0
    rect.height = 100.0

    print ('Point with position x:', point.x, 'y:', point.y)
    print ('Circle of radius', circ.radius ,', centre point is x:', circ.centre.x, 'y:', circ.centre.y)
    print ('Rectangle with top left point x:', rect.corner.x, 'y:', rect.corner.y, 'width', rect.width, 'height', rect.height)
    print('Does Point lie on or within the circle?:', point_in_circle(circ, point))
    print('Does the rectangle lie entirely within or on the boundaries of the circle?:', rect_in_circle(circ, rect))
    print('Do any corners of the rectangle lie within or on the boundaries of the circle?:', rect_corners_and_circle_overlap(circ, rect))
    print('Does any part of the rectangle fall inside the circle?:', rect_inside_circle(circ, rect))
 
    bob = turtle.Turtle()
    draw_axes(bob, 200)
    draw_rect(bob, rect)
    draw_circle(bob, circ)
    turtle.mainloop()

       
main()
