def recurse(n, s):
    """ Calculates n factorial recursively
    """
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)

recurse(3, 0)
