def ack(m, n):
    if m ==0:
        return n + 1
    if m > 0 and n == 0:
        return ack(m-1, 1)
    if m > 0 and n > 0:
        return ack(m - 1, ack(m , n -1))
    else:
        return None

print ('ack(3, 4) =', ack(3, 4))
print ('ack(3, 5) =', ack(3, 5))
print ('ack(3, 6) =', ack(3, 6))
print ('ack(3, 7) =', ack(3, 7))

