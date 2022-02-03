def gcd(a, b):
    if b == 0:
        return a
    else:
        r = a % b
        return gcd(b, r)


print (gcd(50, 100))
print (gcd(81, 3))
