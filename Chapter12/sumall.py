def sumall(*args):
    total = 0
    for i in args:
        total += i
    return total

print(sumall(1, 4.3, 7, -11))
