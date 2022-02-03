def is_power(a, b):
    if a == b:
        return True
    elif a % b != 0:
        return False
    else:
        return is_power(a/b, b)

print (is_power(16, 2))
print (is_power(17, 2))
print (is_power(1, 1))
print (is_power(0, 0))
print (is_power(-8 , -2))
print (is_power(-27, -3))

