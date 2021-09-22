import turtle
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
        
turtle.mainloop

polygon(bob, 20, 6)

