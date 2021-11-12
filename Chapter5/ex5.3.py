def is_triangle(a, b, c):
    """ Checks 3 side lengths to see whether
        they can form a triangle (degenerate triangle returns 'yes')"""
    if a + b < c or b + c < a or a + c < b:
        print ('No')

    else:
        print ('Yes')


def get_input():
    print ('Enter 3 stick lengths (as integers) to find out whether they can form a triangle')
    a = int(input('Enter length a: '))
    b = int(input('Enter length b: '))
    c = int(input('Enter length c: '))

    is_triangle(a, b, c)

get_input()
            
