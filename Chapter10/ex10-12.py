

def interlock(word_list):
    """Finds all pairs of words that interlock to form a word also in the list"""
    for word in word_list:
        first_word = word[0::2]
        second_word = word[1::2]
        if first_word in word_list and second_word in word_list:
            print(word, first_word, second_word)


def interlock3(word_list):
    """Finds all pairs of words that interlock to form a word also in the list"""
    for word in word_list:
        first_word = word[0::2]
        second_word = word[1::2]
        third_word = word[2::2]
        if first_word in word_list and second_word in word_list and third_word in word_list:
            print(word, first_word, second_word, third_word)
        
def in_bisect(word_list, target):
    """ Takes a sorted word list and checks for presence of target word using bisection search"""
    
    split_point = (len(word_list) // 2)
    if target == word_list[split_point]:
        return True
    if len(word_list) <= 1:
        return False
    
    if target < word_list[split_point]:
        return in_bisect(word_list[0:split_point], target)
    else:
        return in_bisect(word_list[split_point:], target)
    




fin = open('words.txt')
l = []
for i in fin:
    l.append(i.strip())

interlock(l)
