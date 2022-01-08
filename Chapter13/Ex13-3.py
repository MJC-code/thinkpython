import string

def process_line(line):
    result = []    
    for word in line.split():
        word = (word.strip(string.whitespace + string.punctuation + '“' + '”'))
        word = word.lower()
        print(word)
    
def remove_header(gutenberg_file):
    for line in gutenberg_file:
        if '*** START OF' in line:
            break


fin = open('jane_austen.txt')
# This text uses open and close quotes which are not part of string.punctuation
remove_header(fin)
for line in fin:
    process_line(line.strip())
