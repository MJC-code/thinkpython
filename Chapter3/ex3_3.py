def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)
    
def print_crosspiece():
    print('+ - - - - ', end='')

def print_crosspieces():
    do_twice(print_crosspiece)
    print('+')

def print_column():
    print('|         ', end='')

def print_columns():
    do_twice(print_column)
    print('|')

def draw_section():
    print_crosspieces()
    do_four(print_columns)

def draw_whole():
    do_twice(draw_section)
    print_crosspieces()

draw_whole()

