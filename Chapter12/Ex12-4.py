reducible_dict = dict()
#reducible_dict['a'] = True
#reducible_dict['i'] = True
reducible_dict[''] = True


def word_dict_setup(filename):
    fin = open(filename)
    word_dict = {}
    for word in fin:
        word_dict[word.strip()] = None
    word_dict['i'] = None
    word_dict['a'] = None
    word_dict[''] = None
    return word_dict


def find_children(word, word_dict):
    res = []
   
    for index in range(len(word)):
        new_word = word[:index] + word[index+1:]

        if new_word in word_dict:
            res.append(new_word)          
        index += 1
        
    return res


def is_reducible(word, word_dict):
    if word in reducible_dict:
        if reducible_dict[word] == True:
            return True
        if reducible_dict[word] == False:
            return False
    else:
        for i in find_children(word, word_dict):
            return is_reducible(i, word_dict)
    reducible_dict[word] = False
    return False
        
def search_for_reducible_words(word_dict):
    longest = 1
    for word in word_dict:
        if len(word) < longest:
            continue
        if is_reducible(word, word_dict):
            reducible_dict[word] = True
            if len(word) >= longest:
                print(word)
                longest = len(word)
            
            
        
    
#find_reducible_words('words.txt')
word_dict = word_dict_setup('words.txt')
#for i in word_dict:
#    reducible_dict[i] = None
#for i in t:
#    print (i)
#print (find_children('sprite', word_dict))
#print(is_reducible('please', word_dict))
search_for_reducible_words(word_dict)

                           
