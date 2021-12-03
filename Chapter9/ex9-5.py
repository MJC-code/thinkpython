
def test_words():
     """Prints all words in words.txt that contain
          all letters from the user inputted string then prints
          what percentage of total this represents"""
     fin = open('words.txt')
     total_words = 0
     counter = 0

     required = input('Please enter a string of required letters: ')
     for line in fin:
          total_words += 1
          word = line.strip()
          if uses_all(word, required):
               counter += 1
               print(word)

     percentage = counter/total_words * 100
     print('Percentage of words using all of the letters', required, 'is: ', percentage)
     

def uses_all(word, required):
     for letter in required:
          if letter not in word:
               return False
     return True
     

def uses_only(word, allowed):
     for letter in word:
          if letter not in allowed:
               return False
     return True

def avoids(word, forbidden):
     for letter in word:
          if letter in forbidden:
               return False
     return True


test_words()
          





