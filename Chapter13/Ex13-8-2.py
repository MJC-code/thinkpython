
import random
import string
import bisect

def process_file(filename, skip_header):
    """Takes a text file from Project Gutenberg as input, breaks it into
    words without removing punctuation
    Returns a list containing every word of text in order"""
    result = []
    fp = open(filename)

    if skip_header:
        skip_gutenberg_header(fp)

    for line in fp:
        if line.startswith('*** END OF TH'):
            break
        process_line(line, result)

    return result


def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.
    fp: open file object
    """
    for line in fp:
        if line.startswith('*** START OF TH'):
            break


def process_line(line, result):
    """ Takes a line from Gutenberg text file, replaces hyphens,
    adds each word to 'result' - a list of the words in the book
    """

    line = line.replace('-', ' ')

    for word in line.split():
        result.append(word)

    
def create_markov_dictionary():
    """Takes a Gutenberg Project text file
    Returns a Markov dictionary, where keys are tuples of prefix_length words,
    values are words that follow each tuple in the text"""
    word_list = process_file('emma.txt', skip_header=True)
    markov_dict = {}
    prefix_length = 2
    
    for i in range(len(word_list)):
        prefix = tuple(word_list[i:i+prefix_length])
        try:
            suffix = word_list[i+prefix_length]
        except IndexError:
            continue
    
        markov_dict[prefix] = markov_dict.get(prefix, []) + [suffix]     

    return markov_dict   

def create_random_text(markov_dict, length):
    """Takes a Markov dictionary.
    Returns a Markov generated text of (length) words"""
    result = []
    prefix_suffix_list = list(markov_dict.items())
    prefix_suffix = random.choice(prefix_suffix_list)
    prefix = prefix_suffix[0]
    suffix = random.choice(prefix_suffix[1])

    for i in range(length):
        result.append(prefix[0])
        
        new_prefix = prefix[1:] + (suffix,)
        new_suffix = random.choice(markov_dict[new_prefix])
        prefix = new_prefix
        suffix = new_suffix
        
        

    print(' '.join(result))


t = create_markov_dictionary()
create_random_text(t, 100)

##if __name__ == '__main__':
##    main()

