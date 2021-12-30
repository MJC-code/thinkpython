def find_special_homophone(pronouncing_dictionary):
    """Takes a pronouncing dictionary, returns a list of words where removing either
of the first two letters gives a homophone of the original word"""
    fin = open('words.txt')
    dictionary_words = []
    for i in fin:
        dictionary_words.append(i.strip())

    results=[]
    
    t = read_dictionary(pronouncing_dictionary)
    
        
    for i in t:
       
        first_missing = t.get(i[1:], 0)
        second_missing = t.get(i[0] + i[2:] , 0)
        if t[i] == first_missing and t[i] == second_missing:
            if i in dictionary_words and i[1:] in dictionary_words and i[0] + i[2:] in dictionary_words:
                results.append(i)
                
    return results
        
        



def read_dictionary(filename='c06d'):
    """Reads from a file and builds a dictionary that maps from
    each word to a string that describes its primary pronunciation.

    Secondary pronunciations are added to the dictionary with
    a number, in parentheses, at the end of the key, so the
    key for the second pronunciation of "abdominal" is "abdominal(2)".

    filename: string
    returns: map from string to pronunciation
    """
    d = dict()
    fin = open(filename)
    for line in fin:

        # skip over the comments
        if line[0] == '#': continue

        t = line.split()
        word = t[0].lower()
        pron = ' '.join(t[1:])
        d[word] = pron

    return d


print(find_special_homophone('c06d'))



