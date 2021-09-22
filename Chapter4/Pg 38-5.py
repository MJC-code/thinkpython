import turtle
import math

bob = turtle.Turtle()

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.rt(90)

def polygon(t, length, n):
    """Draws a polygon using turtle t with n sides of length length"""
    for i in range(n):
        t.fd(length)
        t.rt(360/n)

def polyline(t, length, n, angle):
    """Draws  using turtle t with n sides of length length"""
    for i in range(n):
        t.fd(length)
        t.rt(angle/n)

        
def circle(t, r):
    """Draws a circle of radius r using turtle t"""
    circumference = math.pi * 2 * r
    n = int (circumference / 3)
    length = circumference/n
    polygon(t, length, n)

def arc(t, r, angle):
    circumference = math.pi * 2 * r
    n = int (circumference / 3)
    length = circumference/n * (angle/360)
    polyline(t, length, n, angle)


arc(bob, 40, 90)
circle(bob, 40)
turtle.mainloop
