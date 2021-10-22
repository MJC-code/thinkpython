"""Draws letters with scale n"""


import turtle

# The following definitions are needed to use the typewriter.py function given by the author

def fd(t, length):
    t.fd(length)

def bk(t, length):
    t.bk(length)

def lt(t, angle=90):
    t.lt(angle)

def rt(t, angle=90):
    t.rt(angle)

def pd(t):
    t.pd()

def pu(t):
    t.pu()

def skip(t, n):
    """lift the pen and move"""
    pu(t)
    fd(t, n)
    pd(t)






def draw_a(t, n):
    t.setheading(75)
    t.fd(n*3)
    t.setheading(-75)
    t.fd(n*3)
    t.setheading(0)
    t.pu
    
    
    
