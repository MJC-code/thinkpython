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

    list_of_anagrams = []
    for i in range (len(result)):
        if len(result[i]) > 1:
            list_of_anagrams.append(result[i])
    return list_of_anagrams


def sort_anagram_list(filename):
    """Takes a list of lists of anagrams, sorts by list length high to low
    Returns a list"""
    t = find_anagrams('words.txt')
    res =[]
    lengths = []
    for i in t:
        lengths.append((len(i), i))
    for i in sorted(lengths, reverse = True):
        res.append(i)
    return res
    


t = sort_anagram_list('words.txt')
for i in t:
    print(i)
    

    
