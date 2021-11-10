

def check_fermat(a, b, c, n):
    """Checks whether 4 positive integers obey Fermat's last theorem
    (a**n + b**n = c**n doesn't hold for n>2)"""
    
    for i in [a, b, c, n]:
        if type(i) != int or i < 1:
            print('All inputs must be positive integers')
            return
    if a**n + b**n == c **n and n>2:
        print ('Holy smokes, Fermat was wrong!')
    else:
        print ("No that doesn't work.")

