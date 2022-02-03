def compare(x, y):
    if x > y:
        return 1
    if x < y:
        return -1
    else:
        return 0

print ('Expected outputs are 1, 0, -1')
print(compare(6, 5))
print(compare(4, 4))
print(compare(5, 6))
