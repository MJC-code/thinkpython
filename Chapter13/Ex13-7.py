"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""
### MJC 12/1/22 Corrected strippables to include “ and  ” marks

from __future__ import print_function, division

import random
import string
import bisect

def process_file(filename, skip_header):
    """Makes a histogram that contains the words from a file.

    filename: string
    skip_header: boolean, whether to skip the Gutenberg header
   
    returns: map from each word to the number of times it appears.
    """
    hist = {}
    fp = open(filename)

    if skip_header:
        skip_gutenberg_header(fp)

    for line in fp:
        if line.startswith('*** END OF THIS'):
            break

        process_line(line, hist)

    return hist


def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.

    fp: open file object
    """
    for line in fp:
        if line.startswith('*** START OF THIS'):
            break


def process_line(line, hist):
    """Adds the words in the line to the histogram.

    Modifies hist.

    line: string
    hist: histogram (map from word to frequency)
    """
    # TODO: rewrite using Counter

    # replace hyphens with spaces before splitting
    line = line.replace('-', ' ')
    strippables = string.punctuation + string.whitespace + '“' + '”'

    for word in line.split():
        # remove punctuation and convert to lowercase
        word = word.strip(strippables)
        word = word.lower()

        # update the histogram
        hist[word] = hist.get(word, 0) + 1


def most_common(hist):
    """Makes a list of word-freq pairs in descending order of frequency.

    hist: map from word to frequency

    returns: list of (frequency, word) pairs
    """
    t = []
    for key, value in hist.items():
        t.append((value, key))

    t.sort()
    t.reverse()
    return t


def print_most_common(hist, num=10):
    """Prints the most commons words in a histgram and their frequencies.
    
    hist: histogram (map from word to frequency)
    num: number of words to print
    """
    t = most_common(hist)
    print('The most common words are:')
    for freq, word in t[:num]:
        print(word, '\t', freq)


def subtract(d1, d2):
    """Returns a dictionary with all keys that appear in d1 but not d2.

    d1, d2: dictionaries
    """
    # TODO: reimplement using Counter
    return set(d1) - set(d2)


def total_words(hist):
    """Returns the total of the frequencies in a histogram."""
    return sum(hist.values())


def different_words(hist):
    """Returns the number of different words in a histogram."""
    return len(hist)


def random_word(hist):
    """Chooses a random word from a histogram.

    The probability of each word is proportional to its frequency.
    """
    # TODO: rewrite using Counter
    words = []
    freqs = []
    total_freq = 0

    # make a list of words and a list of cumulative frequencies
    for word, freq in hist.items():
        total_freq += freq
        words.append(word)
        freqs.append(total_freq)

    # choose a random value and find its location in the cumulative list
    x = random.randint(0, total_freq-1)
    index = bisect.bisect(freqs, x)
    return words[index]



def main():
    hist = process_file('emma.txt', skip_header=True)
    print('Total number of words:', total_words(hist))
    print('Number of different words:', different_words(hist))
##
##    t = most_common(hist)
##    print('The most common words are:')
##    for freq, word in t[0:20]:
##        print(word, '\t', freq)
##
##    words = process_file('words.txt', skip_header=False)
##
##    diff = subtract(hist, words)
##    print("The words in the book that aren't in the word list are:")
##    for word in diff:
##        print(word, end=' ')

    print("\n\nHere are some random words from the book")
    for i in range(1):
        print(random_word(hist), end= ' ')
        


if __name__ == '__main__':
    main()


