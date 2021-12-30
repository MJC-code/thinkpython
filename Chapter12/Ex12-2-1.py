def make_anagram_dict(filename):
    """Finds all anagrams in a list of words, returns a dictionary of words-> anagrams"""
    result = {}
    fin = open(filename)
    
    for line in fin:
        word = line.strip().lower()
        letters_in_word = tuple(sorted(word))

        if letters_in_word not in result:
            result[letters_in_word] = [word]
        else:
            result[letters_in_word].append(word)
#    for key, value in result.items():
#        print(key, value)
    return result
    
def find_anagrams(filename):
    result = []
    t = make_anagram_dict(filename)
    for i in t:
        anagrams = []
        for word in t[i]:
            anagrams.append(word)
        if sorted(anagrams) not in anagrams:
            result.append(sorted(anagrams))
    return result


        

t = find_anagrams('words.txt')
for i in t:
    print(i)
    

    
