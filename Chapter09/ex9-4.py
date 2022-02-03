
def test_words():
     """Prints all words in words.txt that use only
          letters from the user inputted string then prints
          what percentage of total this represents"""
     fin = open('words.txt')
     total_words = 0
     counter = 0

     allowed = input('Please enter a string of allowed letters: ')
     for line in fin:
          total_words += 1
          word = line.strip()
          if uses_only(word, allowed):
               counter += 1
               print(word)

     percentage = counter/total_words * 100
     print('Percentage of words using only the letters', allowed, 'is: ', percentage)
     

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

# 5 least used letters are q, j, x, z, w
test_words()
          





