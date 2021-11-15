import turtle
bob = turtle.Turtle()

def draw(t, length, n):
    """ Recursively draws a tree, where each branch splits into 2 smaller branches
        for n generations"""
    if n == 0:
        return
    angle = 30
    t.fd(length * n)
    t.lt(angle)
    draw(t, length, n-1)
    t.rt(2* angle)
    draw(t, length, n-1)
    t.lt(angle)
    t.bk(length * n)

draw(bob, 10, 4)
