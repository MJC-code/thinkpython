def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse

def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d

def invert_dict_revised(d):
    inverse = dict()
    for key in d:
        val = d[key]
        print(inverse)
        inverse.setdefault(val, []).append(key)
    return inverse


hist = histogram('parrotrr')
print(invert_dict(hist))
print(invert_dict_revised(hist))


