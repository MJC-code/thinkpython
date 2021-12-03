
def test_words():
     """Prints all words in words.txt whose letters are in
          alphabetical order"""
     fin = open('words.txt')
     total_words = 0
     counter = 0

     
     for line in fin:
          total_words += 1
          word = line.strip()
          if is_abecedarian_2(word):
               counter += 1
               print(word)

     percentage = counter/total_words * 100
     print('Percentage of words that are abecedarian is: ', percentage)
     

def is_abecedarian(word):
     for i in range(len(word)-1):
          if word[i] > word[i+1]:
               return False
     return True

def is_abecedarian_2(word):
     i=0
     while i < len(word) - 1:
          if word[i+1] < word[i]:
               return False
          i = i + 1
     return True


test_words()
          





