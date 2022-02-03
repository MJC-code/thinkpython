
def output():
    print('Hello')



def do_n(f, n):
    if n <= 0:
        return
    else:
        f()
        do_n(f, n - 1)


do_n(output, 10)     
