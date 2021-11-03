"""Draws letters with scale n - most letters are 2n high, 1 n wide """

n = 30 # This is the scaling factor

import turtle
from polygon import arc
import math


def fdbk(t, length):
    t.pd()
    t.fd(length)
    t.bk(length)
    
# primitives of drawing 

def add_space(t, n):
        t.pu()
        t.setheading(0)
        t.fd(n)
        t.pd()

def go_to_bottom_right(t):
    t.pu()
    t.setheading(0)
    t.fd(n)

def go_to_mid_mid(t):
    t.pu()
    t.setheading(0)
    t.fd(n/2)
    t.lt(90)
    t.fd(n)

def go_to_mid_right(t):
    t.pu()
    t.setheading(0)
    t.fd(n)
    t.lt(90)
    t.fd(n)
    t.setheading(0)
    t.pd()

def go_to_bottom_mid(t):
    t.pu()
    t.setheading(0)
    t.fd(n/2)
    t.pd()
    
def bottom_half_circle(t):
    t.pd()
    arc(t, n/2, 360)
    t.pu()
    t.setheading(180)
    t.fd(n/2)
    t.setheading(0)
    
def draw_mid_crosspiece(t):
    t.pu()
    t.setheading(90)
    t.fd(n)
    t.setheading(0)
    t.pd()
    fdbk(t, n)
    t.pu()
    t.setheading(270)
    t.fd(n)

    
# Letter drawing code using primitives defined above
    
def draw_a(t):
    bottom_half_circle(t)
    go_to_bottom_right(t)
    t.setheading(90)
    fdbk(t, n)
    add_space(t, n)

def draw_b(t):
    bottom_half_circle(t)
    t.setheading(90)
    fdbk(t, n*2)
    add_space(t, n)

def draw_c(t):
    add_space(t, n/2)
    go_to_mid_mid(t)
    t.pd()
    t.setheading(180)
    arc(t, n/2, 180)
    add_space(t, n)

def draw_d(t):
    bottom_half_circle(t)
    go_to_bottom_right(t)
    t.setheading(90)
    fdbk(t, n*2)
    add_space(t, n)

def draw_e(t):
    t.pu()
    t.setheading(225)
    t.fd(n*(math.sin(math.radians(45))))
    t.pd()
    draw_mid_crosspiece(t)
    go_to_mid_right(t)
    t.setheading(90)
    arc(t, n/2, 300)
    add_space(t, n)
        
def draw_f(t):
    t.pd()
    t.setheading(90)
    t.fd(n*1.5)
    arc(t, n/3, -180)
    


    
bob = turtle.Turtle()
bob.setheading(0)
#draw_a(bob)
#draw_b(bob)
#draw_c(bob)
#draw_d(bob)
draw_e(bob)
draw_f(bob)
turtle.mainloop()


    
