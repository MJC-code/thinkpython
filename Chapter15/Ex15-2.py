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
    print(circle.centre.x + circle.radius, circle.centre.y)
    t.setheading(90)
    t.pd()
    t.circle(circle.radius)
    t.pu()
    t.goto(0,0)
    t.setheading(0)

    
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
    circ.centre.x = 0
    circ.centre.y = 0
    circ.radius = 50.0

    point = Point()
    point.x = 0
    point.y = 0

    rect = Rectangle()
    rect.corner = Point()
    rect.corner.x = 0
    rect.corner.y = 10
    rect.width = 50.0
    rect.height = 100.0

    bob = turtle.Turtle()
    draw_axes(bob, 200)
    draw_rect(bob, rect)
    draw_circle(bob, circ)
    turtle.mainloop()

    
main()
