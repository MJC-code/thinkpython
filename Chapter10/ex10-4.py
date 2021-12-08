def chop(t):
    """Takes a list, modifies it by removing first and last elements, returns None"""
    del t[-1]
    del t[0]
    return None

t = [1, 2, 3, 4, 5, 6]
chop(t)
print(t)
print (chop(t))

