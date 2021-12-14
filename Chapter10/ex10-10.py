
import time

def in_bisect(word_list, target):
    """ Takes a sorted word list and checks for presence of target word using bisection search"""
    
    split_point = (len(word_list) // 2)
    if target == word_list[split_point]:
        return True
    if len(word_list) <= 1:
        return False
    
    if target < word_list[split_point]:
#        print ('Calling in_bisect on 0', split_point)
        return in_bisect(word_list[0:split_point], target)
    else:
#        print ('Calling in_bisect on', split_point, len(word_list))
        return in_bisect(word_list[split_point:], target)
    

fin = open('words.txt')
l = []
for i in fin:
    l.append(i.strip())

start_time = time.process_time()
print ('zebra' in l)
print ('Finding zebra using in took ', time.process_time() - start_time, 'seconds')

start_time = time.process_time()
print (in_bisect(l, 'zebra'))
print ('Finding zebra using in_bisect took ', time.process_time() - start_time, 'seconds')

start_time = time.process_time()
print ('dfhdfgdfgh' in l)
print ('Finding dfhdfgdfgh using in took ', time.process_time() - start_time, 'seconds')

start_time = time.process_time()
print (in_bisect(l, 'dfhdfgdfgh'))
print ('Finding dfhdfgdfgh using in_bisect took ', time.process_time() - start_time, 'seconds')

