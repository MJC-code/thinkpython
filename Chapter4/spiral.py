"""Draws an Archimedean spiral"""

import turtle
import polygon


bob = turtle.Turtle()


for i in range(200):
    polygon.arc(bob, i, 30)
    

turtle.mainloop()
