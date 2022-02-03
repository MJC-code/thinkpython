import turtle
bob = turtle.Turtle()

def cesaro(t, x):
    """ Draws a Cesaro fractal with length x"""
    if x < 2:
        t.fd(x)
        return
    cesaro(t, x / 3)
    t.lt(85)
    cesaro(t, x / 3)
    t.rt(170)
    cesaro(t, x / 3)
    t.lt(85)
    cesaro(t, x / 3)
    



cesaro(bob, 200)
