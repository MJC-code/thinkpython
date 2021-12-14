

def find_reverse_pairs(word_list):
    """Prints all words in a list that also appear in the list in reversed form"""
    for i in word_list:
        if in_bisect(word_list, i[::-1]):
            print (i, i[::-1])

        
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

find_reverse_pairs(l)
