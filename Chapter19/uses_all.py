def uses_all(word, required):
    return all (letter in word for letter in required)
       

required = 'abcdefg'
word = 'abcdefgxyz'
print (uses_all(word, required))


required = 'abcdefghij'
word = 'abcdefgh'
print (uses_all(word, required))
