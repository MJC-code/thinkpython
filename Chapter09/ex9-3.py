
def test_words():
     """Prints all words in words.txt that do not contain
          any letters from the user inputted string then prints
          what percentage of total this represents"""
     fin = open('words.txt')
     total_words = 0
     counter = 0

     forbidden = input('Please enter a string of forbidden letters: ')
     for line in fin:
          total_words += 1
          word = line.strip()
          if avoids(word , forbidden):
               counter += 1
               print(word)

     percentage = counter/total_words * 100
     print('Percentage of words avoiding the letters', forbidden, 'is: ', percentage)
     

def avoids(word, forbidden):
     for letter in word:
          if letter in forbidden:
               return False
     return True

# 5 least used letters are q, j, x, z, w
test_words()
          





