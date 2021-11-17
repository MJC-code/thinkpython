def b(z):
    prod = a(z, z)
    print (z, prod)
    return prod

def a(x, y):
    x = x + 1
    return x * y

def c(x, y, z):
    total = x + y + z
    square = b(total)**2
    return square

x = 1
y = x + 1
print(c(x, y+3, x+y))


"""Stack diagram:

main__          x -> 1
                y -> 2

c               x -> 1
                y -> 5
                z -> 3
                total -> 9
                square -> 90**2

b               z -> 9
                prod -> 90

a               x -> 10
                y -> 9
"""
