import string
word_usage = dict()

def process_line(line):
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
    for line in gutenberg_file:
        if '*** START OF' in line:
            break

def analyse_book(gutenberg_file):
    """Takes a text file book from Project Gutenberg,
    returns the number of unique words in the book"""
    result = []
    word_usage.clear()
    fin = open(gutenberg_file)
    remove_header(fin)
    for line in fin:
        if '*** END OF' in line:
            break
        process_line(line.strip())
    for word in sorted(word_usage, key=word_usage.get, reverse = True):
        result.append(word)
    return result[0:20]


# This text uses open and close quotes which are not part of string.punctuation
d = analyse_book('pride_and_prejudice.txt')
print('Pride and Prejudice top 20 words are:', d, '\n')


d = analyse_book('gatsby.txt')
print('The Great Gatsby top 20 words are:', d, '\n')

d = analyse_book('defoe.txt')
print('Robinson Crusoe top 20 words are:' , d, '\n')

d = analyse_book('maugham.txt')
print('Of Human Bondage top 20 words are:', d, '\n')




