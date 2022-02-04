class Point:
    """Defines a point object
    Attributes are x and y, floats representing x and y position"""
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __str__(self):
        return '(%.2f, %.2f)' % (self.x, self.y)

    def __add__(self, other):
        if isinstance(other, Point):
            result = self.add_point_to_self(other)
        else:
            result = self.add_tuple_to_self(other)
        return result

    def __radd__(self, other):
            return self.__add__(other)

    def add_point_to_self(self, other):
        result = Point()
        result.x = self.x + other.x
        result.y = self.y + other.y
        return result

    def add_tuple_to_self(self, other):
        result = Point()
        result.x = self.x + other[0]
        result.y = self.y + other[1]
        return result


p1 = Point(2, 7)
p2 = Point(3, 6)
p3 = p1 + p2
print(p1, p2, p3)
p3 = (20, 25) + p2
print(p1, p2, p3)



    


        

