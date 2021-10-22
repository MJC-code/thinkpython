"""Draws letters with scale n"""

import turtle
import polygon
import math

def fdbk(t, n):
    t.fd(n)
    t.bk(n)

def add_space(t, n):
        t.pu()
        t.setheading(0)
        t.fd(n / 3)
        t.pd()
        
def draw_a(t, n):
    t.setheading(75)
    t.fd(2*n / math.sin (math.radians(75)))
    t.setheading(-75)
    t.fd(2*n / math.sin (math.radians(75)))
    t.lt(180)
    t.fd(n / math.sin (math.radians(75)))
    t.setheading(180)
    fdbk(t, n/2)
    t.setheading(-75)
    t.fd(n / math.sin (math.radians(75)))
    add_space(t, n)
    
def draw_b(t, n):
    t.setheading(0)
    polygon.arc(bob, n/2, 180)
    t.setheading(0)
    polygon.arc(bob, n/2, 180)
    t.setheading(270)
    t.fd(2 * n)
    t.setheading(0)
    t.pu()
    t.fd(n)
    add_space(t, n)

def draw_c(t, n):
    t.pu()
    t.setheading(90)
    t.fd(n * 2)
    t.rt(90)
    t.fd(n/3)
    t.setheading(180)
    t.pd()
    polygon.arc(bob, n, 180)
    add_space(t, n)
    
def draw_d(t, n):
    t.setheading(0)
<<<<<<< HEAD
    t.pu
    
=======
    polygon.arc(bob, n, 180)
    t.setheading(270)
    t.fd(n*2)
    add_space(t, 4*n)

def draw_e(t, n):
    t.setheading(90)
    t.fd(2 * n)
    t.rt(90)
    fdbk(t, n)
    t.setheading(270)
    t.fd(n)
    t.lt(90)
    fdbk(t, n)
    t.setheading(270)
    t.fd(n)
    t.lt(90)
    
    t.fd(n)
    add_space(t, n)
>>>>>>> aaf6407d5c408979992ca9bc2c48816d5177452a
    
    
scale = 30
bob = turtle.Turtle()
draw_a(bob, scale)

draw_b(bob, scale)
draw_c(bob, scale)
draw_d(bob, scale)
draw_e(bob, scale)
turtle.mainloop()


    
