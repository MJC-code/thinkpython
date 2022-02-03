def is_between(x, y, z):
    """Returns true if x <= y <= x or False otherwise"""
    if x <= y and y <= z:
        return True
    else:
        return False
