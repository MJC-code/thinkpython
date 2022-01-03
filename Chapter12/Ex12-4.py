reducible_dict = dict()
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
            reducible_dict[i] = is_reducible(i, word_dict)
            return reducible_dict[i]

    reducible_dict[word] = False
    return False

        
def search_for_reducible_words(word_dict):
    result = {}
    for word in word_dict:
        if is_reducible(word, word_dict):
            reducible_dict[word] = True
            result[word] = (len(word), find_reducible_chain(word, word_dict))
    return result
            
def find_reducible_chain(word, word_dict):
    result = ''
    for child in find_children(word, word_dict):

        if is_reducible(child, word_dict):
            result = result + child + '-->' + find_reducible_chain(child, word_dict)
    return result


def find_longest_reducible_words(word_dict):
    d = search_for_reducible_words(word_dict)
    result = []
    for word in sorted(d, key=d.get, reverse=True):
        result.append((word, d[word]))
        

    return result[0:5]
    

word_dict = word_dict_setup('words.txt')

t = find_longest_reducible_words(word_dict)
for i in t:
    print(i, '\n')


                           
