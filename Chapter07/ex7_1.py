import math

def mysqrt(a):
     epsilon = 0.0000001
     x = a / 2

     while True:
         y = (x + a/x) / 2
         if abs (y-x) < epsilon:
             break
         x = y
    
     return y



def test_square_root(maximum):
    i = 1
    print ('{:<5}'.format('a'), '{:<25}'.format('mysqrt(a)'), '{:<25}'.format('math.sqrt(a)'), '{:<25}'.format('diff'))
    print ('{:<5}'.format('-'), '{:<25}'.format('---------'), '{:<25}'.format('------------'), '{:<25}'.format('----'))

    while (i <= maximum):
        print ('{:<5}'.format(i), '{:<25}'.format(mysqrt(i)), '{:<25}'.format(math.sqrt(i)), '{:<25}'.format(abs(mysqrt(i) - math.sqrt(i))))
        i += 1
        
            
       
    
test_square_root(100)
