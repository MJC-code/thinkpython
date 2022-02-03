
def test_words():
     """Prints all words in words.txt containing no 'e', then prints
          what percentage of total this represents"""
     fin = open('words.txt')
     total_words = 0
     no_e_words = 0
     
     for line in fin:
          total_words += 1
          word = line.strip()
          
          if no_e(word):
               no_e_words += 1
               print(word)
     percentage_no_e_words = no_e_words/total_words * 100
     print('Percentage of words containing no "e" is: ', percentage_no_e_words)
          


def no_e(word):
     for letter in word:
          if letter == 'e':
               return False
     return True

test_words()
          

