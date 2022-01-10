import string

def process_line(line):
    """Takes a line of text from Project Gutenberg, strips punctuation,
    converts words to lower case and prints each word"""
    result = []    
    for word in line.split():
        word = word.replace('-', ' ')
        word = (word.strip(string.whitespace + string.punctuation + '“' + '”'))
        word = word.lower()
        print(word)
    

fin = open('jane_austen.txt')
# This text uses open and close quotes which are not part of string.punctuation

for line in fin:
    process_line(line.strip())
