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
    """Takes a text file word list, returns a list of anagrams found in word list"""
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
    Returns a list of duples - length of words, list of anagrams"""
    t = find_anagrams('words.txt')
    res = []
    lengths = []
    for i in t:
        lengths.append((len(i), i))
    for i in sorted(lengths, reverse = True):
        res.append(i)
    return res

def find_most_anagrams_of_length_n(filename, n):
    
    result = []
    t = make_anagram_dict(filename)
    for i in t:
        anagrams = []
        if len(i) == n:
            for word in t[i]:
                anagrams.append(word)
            if sorted(anagrams) not in anagrams:
                result.append(sorted(anagrams))
    answer = []
    lengths_dict = {}
    for i in result:
        if len(i) > 1:
            if len(i) not in lengths_dict:
                lengths_dict[len(i)] = [i]
            else:
                lengths_dict[len(i)].append(i)

    for k, v in sorted(lengths_dict.items(), reverse=True):
        answer.append(v)
    return answer[0]
        

        


t = find_most_anagrams_of_length_n('words.txt', n=8)
print(t)

    
