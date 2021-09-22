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

def circle(t, r):
    circumference = math.pi * 2 * r
    n = int (circumference / 3)
    print(n)
    length = circumference/n
    polygon(t, length, n)
    
turtle.mainloop

circle(bob, 20)

