def most_frequent(s):
    """Takes a string s and returns list of letters in decreasing order of frequency"""
    histogram = dict()
    for letter in s.lower():
        histogram[letter] = histogram.get(letter, 0) + 1
    
    
    freq_letter_pairs = []
    for letter, freq in histogram.items():
        if letter.isalpha():
            freq_letter_pairs.append((freq, letter))
    

    freq_letter_pairs.sort(reverse = True)
    result = []
    for freq, letter in freq_letter_pairs:
        result.append(letter)
    return result

def open_file_as_string(filename):
    """Takes a filename as a string, returns text of file as a string"""
    fin = open(filename)
    s = ""
    for i in fin:
        s += (i.strip())
    return s
    

print("Letters in decreasing frequency for English text", most_frequent(open_file_as_string('jane_austen.txt')))
print("Letters in decreasing frequency for Italian text", most_frequent(open_file_as_string('italian_beltramelli.txt')))
print("Letters in decreasing frequency for German text", most_frequent(open_file_as_string('german_text.txt')))
