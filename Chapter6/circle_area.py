import math

def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    result = math.sqrt(dsquared)
    return result

def area(radius):
    a = math.pi * radius**2
    return a
    
def circle_area(xc, yc, xp, yp):
    radius = distance(xc, yc, xp, yp)
    circle_area = area(radius)
    return circle_area

circle_area(1, 1, 3, 2)
    
