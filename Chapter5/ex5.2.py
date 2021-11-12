

def check_fermat(a, b, c, n):
    """Checks whether 4 positive integers obey Fermat's last theorem
(a**n + b**n = c**n doesn't hold for n>2)
    """
    for i in [a, b, c, n]:
        if i < 1:
            print('Please enter 4 positive integers')
            return
        
    if a**n + b**n == c**n and n>2:
        print ('\nHoly smokes, Fermat was wrong!')
    else:
        print ("\nNo that doesn't work.")


def input_fermat():
    """ Asks the user to imput 4 values, converts them to integers, then uses
    check_fermat to check whether they violate Fermat's theorem"""
    
    print("You will be asked to input 4 values. They will then be tested to check\n\
whether they violate Pascal's Last Theorem (There are no positive integers\n\
such that a**n + b**n = c**n for n>2")
    
    a = int(input('Enter a positive integer a:\n'))
    b = int(input('Enter a positive integer b:\n'))
    c = int(input('Enter a positive integer c:\n'))
    n = int(input('Enter a positive integer n:\n'))
    
    check_fermat(a, b, c, n)

