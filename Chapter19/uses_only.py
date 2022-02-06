def uses_only(word, available):
    return set(word) <= set(available)


       

available = 'abcdefg'
word = 'abcdefgxyz'
print (uses_only(word, available))


available = 'abcdefghij'
word = 'abcdefgh'
print (uses_only(word, available))
