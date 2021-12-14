"""Compare two ways of making a list from words.txt. Append method is much quicker,
because appending to a list has a constant time cost"""

import time

def test_append_method():
    fin = open('words.txt')
    t = []
    start_time = time.process_time()
    for i in fin:
        t.append(i)
    print('Append method time taken is ', time.process_time() - start_time, 'seconds')

        
def test_add_method():
    fin = open('words.txt')
    t = []
    start_time = time.process_time()
    for i in fin:
        t = t + [i]
    print('Add method time taken is ', time.process_time() - start_time, 'seconds')

test_append_method()

test_add_method()
