
import random
import string
import math

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

def create_freq_dict(text_file):
    """Reads text from a file, counts word frequencies, prints one line for
    each word in descending order"""
    freqs = dict()
    fin = open(text_file)
    skip_gutenberg_header(fin)

    strippables = (string.whitespace + string.punctuation + '“' + '”' + '-')
    for line in fin:
        if line.startswith('*** END OF TH'):
            break
        line = line.replace('-', ' ')
        for word in line.split():
            word = word.translate(str.maketrans('', '', strippables))
            word = word.lower()
            freqs[word] = freqs.get(word, 0) + 1
    return freqs

def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.
    fp: open file object
    """
    for line in fp:
        if line.startswith('*** START OF TH'):
            break

freqs = create_freq_dict("emma.txt")

sorted_freqs = sorted(freqs.items(), key=lambda x: x[1], reverse=True)
freq_logs = []
rank_logs = []
for rank in range(len(sorted_freqs)):
    rank_logs.append(math.log(rank + 1))
    freq_logs.append(math.log(sorted_freqs[rank][1]))



plt.title('Zipf plot')
plt.xlabel('rank')
plt.ylabel('frequency')
plt.plot(rank_logs, freq_logs)
plt.show()
