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
    polygon.arc(t, n/2, 180)

def inverted_loop(t, n):
    t.pd()
    polygon.arc(t, n/2, -180)

def arrow(t, n):
    t.lt(70)
    t.fd((2*n)/math.sin(math.radians (70)))
    t.rt(140)
    t.fd((2*n)/math.sin(math.radians (70)))

""" All definitions below start and end from bottom left corner of letter
"""
def semicircle_bottom(t, n):
    t.setheading(90)
    t.pu()
    t.fd(n)
    t.pd()
    t.setheading(270)
    t.fd(n/2)
    polygon.arc(t, n/2 , 180)
    t.fd(n/2)
    t.setheading(180)
    t.pu()
    t.fd(n)
    t.lt(90)
    t.fd(n)
    t.setheading(0)
    t.pd()

def semicircle_top(t, n):
    t.setheading(90)
    t.pu()
    t.fd(n)
    t.pd()
    t.fd(n/2)
    polygon.arc(t, n/2 , -180)
    t.fd(n/2)
    t.setheading(180)
    t.pu()
    t.fd(n)
    t.lt(90)
    t.fd(n)
    t.setheading(0)
    t.pd()

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

def top_diagonal(t, n):
    t.setheading(90)
    t.pu()
    t.fd(n)
    t.pd()
    t.rt(45)
    fdbk(t, n / math.cos(math.radians(45)))
    t.pu()
    t.setheading(270)
    t.fd(n)
    t.setheading(0)

def bottom_diagonal(t, n):
    t.setheading(90)
    t.pu()
    t.fd(n)
    t.pd()
    t.rt(135)
    fdbk(t, n / math.cos(math.radians(45)))
    t.pu()
    t.setheading(270)
    t.fd(n)
    t.setheading(0)

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
    t.setheading(0)
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
    t.setheading(180)
    loop(t, n * 2)
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
    t.setheading(180)
    loop(t, n * 2)
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
    semicircle_bottom(t, n)
    space(t, n)

def draw_k(t, n):
    left_bottom(t, n)
    left_top(t, n)
    top_diagonal(t, n)
    bottom_diagonal(t, n)
    space(t, n)


def draw_l(t, n):
    bottom_beam(t, n)
    left_bottom(t, n)
    left_top(t, n)
    space (t, n)

def draw_m(t, n):
    t.pu()
    t.fd(n * 1.5)
    t.pd()
    t.lt(90)
    t.fd(n * 2)
    t.setheading(180)
    arrow(t, n)
    t.setheading(270)
    t.fd(n * 2)
    space(t, n)

def draw_n(t, n):
    t.setheading(90)
    t.fd(2 * n)
    t.setheading(300)
    t.fd(2*n / math.cos(math.radians(30)))
    t.setheading(90)
    fdbk(t, 2*n)
    space(t, n/3)
    
def draw_o(t, n):
    semicircle_bottom(t, n)
    semicircle_top(t, n)
    space(t, n)
    
def draw_p(t, n):
    t.setheading(90)
    t.fd(n)
    t.setheading(0)
    loop(t, n)
    t.setheading(270)
    t.fd(2 * n)
    space(t, n / 1.75)

def draw_q(t, n):
    semicircle_bottom(t, n)
    semicircle_top(t, n)
    bottom_diagonal(t, n)
    space(t, n)
    
def draw_r(t, n):
    bottom_diagonal(t, n)
    t.setheading(90)
    t.fd(n)
    t.setheading(0)
    loop(t, n)
    t.setheading(270)
    t.fd(n*2)
    space(t, n)

def draw_s(t, n):
    t.setheading(0)
    loop(t, n)
    t.setheading(180)
    inverted_loop(t, n)
    t.setheading(270)
    t.pu()
    t.fd(2 * n)
    space(t, n / 1.75)


def draw_t(t, n):
    top_beam(t, n)
    t.fd(n / 2)
    left_bottom(t, n)
    left_top(t, n)
    space(t, n * 0.75)

def draw_u(t, n):
    left_top(t, n)
    right_top(t, n)
    semicircle_bottom(t, n)
    space(t, n)

def draw_v(t,n):
    t.pu()
    t.setheading(90)
    t.fd(n * 2)
    t.rt(90)
    t.fd(n)
    t.setheading(180)
    t.pd()
    arrow(t, n)
    t.pu()
    t.setheading(270)
    t.fd(n * 2)
    space(t, n)

def draw_w(t,n):
    t.pu()
    t.setheading(90)
    t.fd(n * 2)
    t.rt(90)
    t.fd(n * 3)
    t.setheading(180)
    t.pd()
    arrow(t, n)
    t.setheading(180)
    arrow(t, n)
    t.pu()
    t.setheading(270)
    t.fd(n * 2)
    space(t, n * 2)

def draw_x(t, n):
    t.setheading(70)
    t.fd(2*n / math.sin(math.radians(70)))
    t.setheading(180)
    t.pu()
    t.fd(2 * n / math.tan(math.radians(70)))
    t.pd()
    t.setheading(290)
    t.fd(2*n / math.sin(math.radians(70)))
    space(t, n/2)

def draw_y(t, n):
    t.setheading(70)
    t.fd(2*n / math.sin(math.radians(70)))
    t.lt(180)
    t.fd(n / math.sin(math.radians(70)))
    t.rt(140)
    fdbk(t, (n / math.sin(math.radians(70))))
    t.setheading(270)
    t.pu()
    t.fd(n)
    space(t, n/2)
    
def draw_z(t, n):
    top_beam(t, n)
    bottom_beam(t, n)
    t.setheading(63.8)
    fdbk(t, 2 * n / math.sin(math.radians(63.8)))
    space(t, n)
    
scale = 10
bob = turtle.Turtle()
bob.pu()
bob.setheading(180)
bob.fd(400)
bob.setheading(0)
bob.pd()


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
draw_k(bob, scale)
draw_l(bob, scale)
draw_m(bob, scale)
draw_n(bob, scale)
draw_o(bob, scale)
bob.pu()
bob.setheading(270)
bob.fd(scale * 3)
bob.rt(90)
bob.fd(scale * 25)
bob.pd()
draw_p(bob, scale)
draw_q(bob, scale)
draw_r(bob, scale)
draw_s(bob, scale)
draw_t(bob, scale)
draw_u(bob, scale)
draw_v(bob, scale)
draw_w(bob, scale)
draw_x(bob, scale)
draw_y(bob, scale)
draw_z(bob, scale)

turtle.mainloop()


    
