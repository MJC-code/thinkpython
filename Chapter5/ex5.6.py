import turtle
bob = turtle.Turtle()

def koch(t, x):
    """ Draws a Koch curve with length x"""
    if x < 3:
        t.fd(x)
        return
    koch(t, x / 3)
    t.lt(60)
    koch(t, x / 3)
    t.rt(120)
    koch(t, x / 3)
    t.lt(60)
    koch(t, x / 3)
    

def snowflake(t, n):
    """Draws a snowflake made of 3 Koch curves of length n"""
    for i in range(3):
        koch(t, n)
        t.rt(120)


snowflake(bob, 100)
turtle.mainloop()
