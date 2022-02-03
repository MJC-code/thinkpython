import turtle
import math

bob = turtle.Turtle()



def polygon(t, length, n):
    """Draws a polygon using turtle t with n sides of length length"""
    for i in range(n):
        angle = 360.0 / n
        polyline(t, length, n, angle)

def polyline(t, length, n, angle):
    """Draws  using turtle t with n sides of length length"""
    for i in range(n):
        t.fd(length)
        t.rt(angle)

        
def circle(t, r):
    """Draws a circle of radius r using turtle t"""
    arc(t, r, 360)

def arc(t, r, angle):
    arc_length = math.pi * 2 * r * angle / 360
    n = int (arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, step_length, n, step_angle)


arc(bob, 40, 90)

turtle.mainloop
