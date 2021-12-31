def find_metathesis_pair(filename):
    """Takes a word list as text file, returns a list of word pairs that can
    be created by swapping one pair of letters"""
    res = []
    t = find_anagrams(filename)
    
    for i in t:
        possibles = i
        
        for x in range(len(possibles)):
            for y in range(len(possibles)):
                if is_swappable(possibles[x], possibles[y]):
                    res.append((possibles[x], possibles[y]))

    return res
            


def is_swappable(word1, word2):
    """Input: 2 strings of equal length
    Returns True if Word2 can be formed by swapping 2 letters in Word1, else False"""
    differing_letter_positions = []
    index = 0
    for i in word1:
        if word1[index] != word2[index]:
            differing_letter_positions.append(index)
        index += 1
    if len(differing_letter_positions) != 2:
        return False
    word2 = list(word2)
    index1 = differing_letter_positions[0]
    index2 = differing_letter_positions[1]
    word2[index1], word2[index2] = word2[index2], word2[index1]
    if list(word1) == (word2):
        return True
    return False
    
    
def make_anagram_dict(filename):
    """Takes a text file containing one word per line.
    Returns a dictionary:
    Key is an alphabetised duple of letters in each word,
    Value is a list of all words that can be formed by those letters"""
    result = {}
    fin = open(filename)
    
    for line in fin:
        word = line.strip().lower()
        letters_in_word = tuple(sorted(word))

        if letters_in_word not in result:
            result[letters_in_word] = [word]
        else:
            result[letters_in_word].append(word)
    return result

    
def find_anagrams(filename):
    """Takes a text file word list, returns an alphabetised list of lists of
    anagrams found in the word list"""
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
    """Takes a list of lists of anagrams
    Returns a list of duples - number of letters(sorted high to low), list of anagrams
    for those letters"""
    t = find_anagrams('words.txt')
    res = []
    lengths = []
    for i in t:
        lengths.append((len(i), i))
    for i in sorted(lengths, reverse = True):
        res.append(i)
    return res



t = find_metathesis_pair('words.txt')
for i in t:
    print(i)

    
