"""Draws letters with scale n - most letters are 2n high and 1n wide"""

import turtle
import polygon
import math


""" All definitions below start and end in bottom left corner of letter
"""

def fdbk(t, n):
    t.pd()
    t.fd(n)
    t.lt(180)
    t.fd(n)
    t.lt(180)


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

def top_beam(t,n):
    t.setheading(90)
    t.pu()
    t.fd(2*n)
    bottom_beam(t, n)
    t.setheading(270)
    t.pu()
    t.fd(2*n)
    t.setheading(0)

def space(t, n):
    t.setheading(0)
    t.pu()
    t.fd(2 * n)
    t.pd()

""" Individual letter definitions"""
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


def draw_l(t, n):
    bottom_beam(t, n)
    left_bottom(t, n)
    left_top(t, n)
    space (t, n)
    
scale = 30
bob = turtle.Turtle()
#left_bottom(bob, scale)
#left_top(bob, scale)
#right_bottom(bob, scale)
#right_top(bob, scale)
#draw_e(bob, scale)
#draw_f(bob, scale)
#draw_h(bob, scale)
#draw_i(bob, scale)
draw_l(bob, scale)
turtle.mainloop()


    
