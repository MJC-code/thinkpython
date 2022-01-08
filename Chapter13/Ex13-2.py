import string
word_usage = dict()

def process_line(line):
    line = line.replace('-', ' ' )
    line = line.replace('—', ' ' )
    for word in line.split():
        word = (word.strip(string.whitespace + string.punctuation + '“' + '”'))
        word = word.lower()
        if word not in word_usage:
            word_usage[word] = 1
        else:
            word_usage[word] += 1
    
            
def remove_header(gutenberg_file):
    for line in gutenberg_file:
        if '*** START OF' in line:
            break

def analyse_book(gutenberg_file):
    """Takes a text file book from Project Gutenberg,
    returns a dictionary of word usage -> frequency"""
    word_usage.clear()
    fin = open(gutenberg_file)
    remove_header(fin)
    for line in fin:
        if '*** END OF' in line:
            break
        process_line(line.strip())
    return word_usage


# This text uses open and close quotes which are not part of string.punctuation
d = analyse_book('pride_and_prejudice.txt')
count = 1
for i in d:
    print(count, i)
    count += 1

