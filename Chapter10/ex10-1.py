def nested_sum(t):
    """Takes a list of lists of integers and returns sum of all their elements"""
    total = 0
    for item in t:
        total += sum(item)
    return total


t = [[1, 2], [3], [4, 5, 6]]
print(nested_sum(t))

