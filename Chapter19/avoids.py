

def avoids(word, forbidden):
    return (set(word) - set(forbidden)) == set(word)
       

forbidden = 'abcdefg'
word = 'abcdefgxyz'
print (avoids(word, forbidden))


forbidden = 'abcdefghij'
word = 'klmn'
print (avoids(word, forbidden))
