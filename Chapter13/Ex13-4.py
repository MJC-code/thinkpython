import string
word_usage = dict()
d = open('words.txt') # open a text file of dictionary words
word_list = dict()
for i in d:
    word_list[i.strip()] = None
word_list['i'] = None
word_list['a'] = None
    

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
    """Takes a text file book from Project Gutenberg,
    returns a list of the 20 most used words in the book"""
    result = []
    word_usage.clear()
    fin = open(gutenberg_file)
    remove_header(fin)
    for line in fin:
        if '*** END OF' in line:
            break
        process_line(line.strip())
    for word in sorted(word_usage, key=word_usage.get, reverse = True):
        if word not in word_list:
            result.append(word)
    return result


# This text uses open and close quotes which are not part of string.punctuation
d = analyse_book('pride_and_prejudice.txt')
print('Pride and Prejudice words not in word list are:\n')
for word in d:
    print(word)


d = analyse_book('gatsby.txt')
print('The Great Gatsby words not in word list are:\n')
for word in d:
    print(word)

d = analyse_book('defoe.txt')
print('Robinson Crusoe words not in word list are:\n')
for word in d:
    print(word)

d = analyse_book('maugham.txt')
print('Of Human Bondage words not in word list are:\n')
for word in d:
    print(word)
