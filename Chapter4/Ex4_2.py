from polygon import arc
import turtle

bob = turtle.Turtle()
turtle.speed(speed=100)
turtle.delay(0)

petals = 16
angle = 30
radius = 10000/ angle

def draw_petal(t, radius, angle):
    for i in range(2):
        arc(t, radius, angle)
        t.lt(180-angle)
            
for i in range(petals):
    draw_petal(bob, radius, angle)
    bob.lt(360 / petals)
    



turtle.mainloop()
