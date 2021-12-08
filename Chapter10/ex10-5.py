def is_sorted(t):
    """Takes a list, returns True if list sorted in ascending order, else False"""
    t2 = sorted(t)
    return t2 == t
        

t = [1, 2, 3, 4, 5, 6]
print(is_sorted(t))
t = [4, 2, 3, 4, 5, 6]
print(is_sorted(t))
t = ['a', 'b', 'c', 'd']
print(is_sorted(t))
t = ['a', 'b', 'c', 'd', 'x', 'w']
print(is_sorted(t))
