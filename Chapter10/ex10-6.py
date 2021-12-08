def is_anagram(word1, word2):
    """Takes 2 strings, returns True if words are anagrams, otherwise False"""
    w1 = list(word1)
    w2 = list(word2)
    w1.sort()
    w2.sort()
    return w1 == w2
    




print (is_anagram('abcedfg', 'gfedcba'))

print (is_anagram('catt', 'tac'))

print (is_anagram('abcedf', 'gfedcba'))

print (is_anagram('a', 'a'))
