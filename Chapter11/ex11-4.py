def has_duplicates(t):
    """Takes a list returns True if any element appears more than once, otherwise False"""
    seen = {}
    for item in t:
        if item in seen:
            return True
        else:
            seen[item] = True  
    return False
    



t = ['a', 'b','c', 'd']
print (has_duplicates(t))


t = ['a', 'b','c', 'd', 'c']
print (has_duplicates(t))


t = [9, 3, 67, 3, 8, 9, 32]
print (has_duplicates(t))
