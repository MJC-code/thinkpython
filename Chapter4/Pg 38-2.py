import turtle
bob = turtle.Turtle()

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.rt(90)

turtle.mainloop

square(bob, 200)
square(bob, 20)
square(bob, 100)
