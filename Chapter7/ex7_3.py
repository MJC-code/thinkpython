import math

def estimate_pi():
     """Computes pi using Ramananujan's infinite series"""
     epsilon = 1e-15
     sum = 0
     k = 0
     factor = 2 * math.sqrt(2) / 9801
     

     while True:
          term = factor * (math.factorial(4 * k) * (1103 + 26390 * k)) / ((math.pow(math.factorial(k), 4)) * math.pow(396, 4 * k))
          sum = sum + term
          print(k, term , sum, 1/sum)
          if term < abs(epsilon):
               break
          k = k + 1
     return 1 / sum   
     
print('Approximation of pi = ', estimate_pi())
