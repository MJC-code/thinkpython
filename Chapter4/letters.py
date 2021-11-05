"""Draws letters with scale n - most letters are 2n high and 1n wide"""

import turtle
import polygon
import math



def fdbk(t, n):
    t.pd()
    t.fd(n)
    t.lt(180)
    t.fd(n)
    t.lt(180)

def loop(t, n):
    t.pd()
    t.setheading(0)
    polygon.arc(t, n/2, 180)

def inverted_loop(t, n):
    t.pd()
    t.setheading(180)
    polygon.arc(t, n/2, 180)

def arrow(t, n):
    t.lt(70)
    t.fd((2*n)/math.sin(math.radians (70)))
    t.rt(140)
    t.fd((2*n)/math.sin(math.radians (70)))

""" All definitions below start and end in bottom left corner of letter
"""


def left_bottom(t, n):
    t.pd()
    t.setheading(90)
    fdbk(t, n)
    t.setheading(0)

def left_top(t, n):
    t.setheading(90)
    t.pu()
    t.fd(n)
    t.pd()
    fdbk(t,n)
    t.pu()
    t.setheading(270)
    t.fd(n)
    t.setheading(0)

def right_bottom(t, n):
    t.setheading(0)
    t.pu()
    t.fd(n)
    t.pd()
    left_bottom(t,n)
    t.setheading(180)
    t.pu()
    t.fd(n)
    t.setheading(0)

def right_top(t, n):
    t.setheading(0)
    t.pu()
    t.fd(n)
    t.pd()
    left_top(t,n)
    t.setheading(180)
    t.pu()
    t.fd(n)
    t.setheading(0)

def bottom_beam(t, n):
    t.setheading(0)
    t.pd()
    fdbk(t, n)

def mid_beam(t,n):
    t.setheading(90)
    t.pu()
    t.fd(n)
    bottom_beam(t, n)
    t.setheading(270)
    t.pu()
    t.fd(n)
    t.setheading(0)
    t.pd()

def top_beam(t,n):
    t.setheading(90)
    t.pu()
    t.fd(2*n)
    bottom_beam(t, n)
    t.setheading(270)
    t.pu()
    t.fd(2*n)
    t.setheading(0)

def left_hook(t, n):
    t.fd(n/2)
    polygon.arc(t, n/2, 90)
    t.lt(180)
    polygon.arc(t, n/2, -90)
    t.fd(n/2)
    t.lt(180)
    

def right_hook(t, n):
    t.fd(n/2)
    polygon.arc(t, n/2, -90)
    t.lt(180)
    polygon.arc(t, n/2, 90)
    t.fd(n/2)
    t.lt(180)

def space(t, n):
    t.setheading(0)
    t.pu()
    t.fd(2 * n)
    t.pd()

""" Individual letter definitions"""

def draw_a(t, n):
    mid_beam(t, n)
    t.setheading(180)
    t.pu()
    t.fd(n/3)
    t.setheading(0)
    t.pd()
    arrow(t, n)
    space(t, n/2)
    
def draw_b(t, n):
    loop(t, n)
    loop(t, n)
    t.setheading(270)
    t.fd(2 * n)
    t.setheading(0)
    space(t, n / 1.75)
    

def draw_c(t, n):
    t.pu()
    t.fd(n)
    t.lt(90)
    t.fd(n * 2)
    t.pd()
    inverted_loop(t, n * 2)
    space(t, n / 2)

def draw_d(t, n):
    loop(t, n*2)
    t.setheading(270)
    t.fd(n * 2)
    t.setheading(0)
    space(t, n)
    
def draw_e(t, n):
    bottom_beam(t, n)
    mid_beam(t, n)
    top_beam(t, n)
    left_bottom(t, n)
    left_top(t, n)
    space(t, n)

def draw_f(t, n):
    mid_beam(t, n)
    top_beam(t, n)
    left_bottom(t, n)
    left_top(t, n)
    space(t, n)

def draw_g(t, n):
    t.pu()
    t.fd(n)
    t.lt(90)
    t.fd(n * 2)
    t.pd()
    inverted_loop(t, n * 2)
    t.setheading(90)
    t.fd(n)
    t.lt(90)
    fdbk(t, n/2)
    t.setheading(270)
    t.fd(n)
    space(t, n/1.75)
    
def draw_h(t, n):
    mid_beam(t, n)
    left_bottom(t, n)
    left_top(t, n)
    right_bottom(t, n)
    right_top(t, n)
    space(t, n)

def draw_i(t, n):
    bottom_beam(t, n)
    top_beam(t, n)
    t.fd(n / 2)
    left_bottom(t, n)
    left_top(t, n)
    space(t, n * 0.75)

def draw_j(t, n):
    right_top(t, n)
    right_bottom(t, n)
    bottom_beam(t, n)
    left_bottom(t, n)
    space(t, n)
    
def draw_l(t, n):
    bottom_beam(t, n)
    left_bottom(t, n)
    left_top(t, n)
    space (t, n)

def draw_p(t, n):
    t.setheading(90)
    t.fd(n)
    loop(t, n)
    t.setheading(270)
    t.fd(2 * n)
    space(t, n / 1.75)

def draw_r(t, n):
    t.setheading(90)
    t.fd(n)
    loop(t, n)
    t.setheading(270)
    t.fd(n)
    t.setheading(300)
    t.fd(n / math.cos(math.radians(30)))
    space(t, n / 1.75)
    
scale = 30
bob = turtle.Turtle()
bob.pd()
#left_bottom(bob, scale)
#left_top(bob, scale)
#right_bottom(bob, scale)
#right_top(bob, scale)

draw_a(bob, scale)
draw_b(bob, scale)
draw_c(bob, scale)
draw_d(bob, scale)
draw_e(bob, scale)
draw_f(bob, scale)
draw_g(bob, scale)
draw_h(bob, scale)
draw_i(bob, scale)
draw_j(bob, scale)
draw_l(bob, scale)
draw_p(bob, scale)
draw_r(bob, scale)

turtle.mainloop()


    
