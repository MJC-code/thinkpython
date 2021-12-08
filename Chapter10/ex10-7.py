def has_duplicates(t):
    """Takes a list returns True if any element appears more than once, otherwise False"""
    seen_letters = []
    for i in t:
        if i in seen_letters:
            return True
        else:
            seen_letters.append(i)
    return False
    



t = ['a', 'b','c', 'd']
print (has_duplicates(t))


t = ['a', 'b','c', 'd', 'c']
print (has_duplicates(t))


t = [9, 3, 67, 3, 8, 9, 32]
print (has_duplicates(t))
