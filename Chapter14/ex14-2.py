import anagram_sets
import shelve

def store_anagrams(output_file):
    shelf = shelve.open(output_file, 'n')
    anagram_map = anagram_sets.all_anagrams('words.txt')
    for key, value in anagram_map.items():
        shelf[key] = value
    shelf.close()


def read_anagrams(db_file, word):
    shelf = shelve.open(db_file, 'c')
    signature = anagram_sets.signature(word)
    try:
        return shelf[signature]
    except:
        return None
    


    
    
store_anagrams('anagram_shelf')

print(read_anagrams('anagram_shelf', 'stop'))
