def cumsum(t):
    """Takes a list of numbers, returns a list of the cumulative sums"""
    result = []
    for i in range(len(t)):
        result.append(sum(t[0:i+1]))
    return result
    

t = [1, 2, 3, 4, 5, 6]
print(cumsum(t))

