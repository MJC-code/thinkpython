import string
import random
import pprint
word_usage = dict()

def setup_word_list():
    d = open('words.txt') # open a text file of dictionary words
    word_list = dict()
    for i in d:
        word_list[i.strip()] = None
    word_list['i'] = None
    word_list['a'] = None
    return word_list
        

def process_line(line):
    """Processes lines of text from Project Gutenberg, stripping punctuation,
    converting to lower case and splitting into words. For each word found,
    increments the word count in the global dictionary word_usage"""
    line = line.replace('-', ' ' )
    line = line.replace('—', ' ' )
    for word in line.split():
        word = (word.strip(string.whitespace + string.punctuation + '“' + '”' + '‘' + '’'))
        word = word.lower()
        if word not in word_usage:
            word_usage[word] = 1
        else:
            word_usage[word] += 1
    
            
def remove_header(gutenberg_file):
    """Scans through a text file from Project Gutenberg until the marker
    for the start of the book is found"""
    for line in gutenberg_file:
        if '*** START OF' in line:
            break

def analyse_book(gutenberg_file):
    """Takes a text file book from Project Gutenberg, creates a histogram of word usage,
    returns a list of words in book but not in word_list"""
    result = []
    word_list = setup_word_list()
    fin = open(gutenberg_file)
    remove_header(fin)
    for line in fin:
        if '*** END OF' in line:
            break
        process_line(line.strip())

    for word in word_usage:
        if word not in word_list:
            result.append(word)
    return result


def find_20_most_used_words():
    result = []
    for word in sorted(word_usage, key=word_usage.get, reverse = True):
        result.append(word)
    return(result[0:20])
    
def choose_from_hist(histogram):
    """Takes a dictionary which is a histogram of words -> their frequencies
    Returns a random word from the histogram with probability in proportion to
    frequency"""
    possibles = []
    for word, freq in word_usage.items():
        possibles.extend([word] * freq)

    return random.choice(possibles)
    
    
    

def main():
    d = analyse_book('pride_and_prejudice.txt')
##    print('Total number of words in book is:', sum(word_usage.values()), '\n')
##    print('Number of unique words in book is:', len(word_usage), '\n')
##    print('20 most used words in book are:', find_20_most_used_words())
##    print('Words in the book not found in word list are:')
##    for i in d:
##        if i.isnumeric():
##            continue
##        print (i, end = ' ')

    print('\nA selection of random words from the book:')
    for i in range(1000):
        print(choose_from_hist(d), end = ' ')

    
main()
