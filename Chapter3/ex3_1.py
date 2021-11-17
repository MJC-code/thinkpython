def right_justify(s):
    padding_length = 70 - len(s)
    print(' ' * padding_length + s)

right_justify('test')
right_justify('1234567890' * 7)

