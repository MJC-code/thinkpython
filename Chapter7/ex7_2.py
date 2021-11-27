import math

def eval_loop():
     while True:
          s = input('Please enter a string to evaluate (Enter \'done\' to exit): ')
          if s == 'Done' or s == 'done':
               break
          answer = eval(s)
          print(answer)
     return answer

eval_loop()

