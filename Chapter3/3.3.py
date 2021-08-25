def do_twice(f, value):
    f(value)
    f(value)

def print_spam():
    print('spam')

def print_twice(f):
    print(f)
    print(f)

def do_four(f, value):
    do_twice(f, value)
    do_twice(f, value)
    
do_twice(print_twice, 'spam')
print()
do_four(print_twice, 'spam')


