reducible_dict = dict()
reducible_dict['a'] = True
reducible_dict['i'] = True
reducible_dict[''] = True


def word_list_setup(filename):
    fin = open(filename)
    word_list = []
    for i in fin:
        word_list.append(i.strip())
    word_list.append('i')
    word_list.append('a')
    word_list.append('')
    return word_list


def find_children(word, word_list):
    word = list(word)
    res = []
   
    for index in range(len(word)):
        letters = word[:]
        letters.pop(index)

        if ''.join(letters) in word_list:
            res.append(''.join(letters))          
        index += 1
        
    return res


def is_reducible(word, word_list):
    if word in reducible_dict:
        if reducible_dict[word] == True:
            return True
        else:
            return False
    if word == '':       
        return True
    else:
        for i in find_children(word, word_list):
            return is_reducible(i, word_list)
    reducible_dict[word] = False
    return False
        
def search_for_reducible_words(word_list):
    longest = 1
    for word in word_list:
        if len(word) < longest:
            continue
        if is_reducible(word, word_list):
            reducible_dict[word] = True
            if len(word) >= longest:
                print(word)
                longest = len(word)
            
            
        
    
#find_reducible_words('words.txt')
word_list = word_list_setup('words.txt')
#for i in t:
#    print (i)
#print (find_children('sprite', word_list))
#print(is_reducible('please', word_list))
search_for_reducible_words(word_list)

                           
