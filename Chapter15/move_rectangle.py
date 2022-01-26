import math
class Point:
    """Represents a point in 2D space"""


def distance_between_points(a, b):
    """ Takes 2 objects of type Point with 'x' and 'y' attributes, returns
        the distance between them"""
    try:
        dx = abs(a.x - b.x)
        dy = abs(a.y - b.y)
    except AttributeError:
        print("distance_between_points requires both arguments to have 'x' and 'y' attributes")
        return None
    return math.sqrt(dx**2 + dy**2)

first = Point()
second = Point()
first.x = 0.0
first.y = 0.0
second.x = 3.0
second.y = 4.0
print(distance_between_points(first, second))
