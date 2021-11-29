def reverse_string():
     s = input('Please enter a string to reverse: ')
     index = len(s)-1
     while index >= 0:
          print(s[index])
          index = index - 1

reverse_string()
