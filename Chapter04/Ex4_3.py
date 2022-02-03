import math
import turtle


def draw_isoceles(top_angle, triangle_height):
    """ Draws an isoceles triangle of height triangle_height, with top_angle in degrees"""
    other_angle = (180 - top_angle) / 2.0
    leg_length = math.sin(math.radians(other_angle)) * triangle_height
    base_length = 2 * math.cos(math.radians(other_angle)) * leg_length
    bob.fd(leg_length)
    bob.lt(180-other_angle)
    bob.fd(base_length)
    bob.lt(180-other_angle)
    bob.fd(leg_length)
    bob.lt(180-top_angle)

def draw_pie(sides, size):
    """Draws a turtle pie with size controlling the height of each isoceles triangle"""
    for i in range(sides):
        draw_isoceles(360/sides, size)
        bob.lt(360/sides)





bob = turtle.Turtle()
#turtle.speed(speed=100)
#turtle.delay(0)

draw_pie(7, 50)
turtle.mainloop()
