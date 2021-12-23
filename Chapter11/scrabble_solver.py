def scrabble_solver(rack_letters):
     """Takes a string rack_letters, returns a list of words that can be formed
using those letters"""
     word_list = {}
     result = []
     histogram_rack_letters = histogram(rack_letters)
     
     fin = open('words.txt')   
     for word in fin:
          word_list[word] = (histogram(word.strip()))
          
     for word, histogram_word_letters in word_list.items():
          if can_be_formed(histogram_word_letters, histogram_rack_letters):
               result.append(word.strip())
     return result




def can_be_formed(histogram_word_letters, histogram_rack_letters):
     """Takes two dictionaries of letter frequencies,
returns True if histogram_word can be formed with letters of histogram_letters"""
     for item in histogram_word_letters:
          if histogram_word_letters[item] > histogram_rack_letters.get(item, 0):
               return False
     return True
          
          

def histogram(s):
     """Takes a string s, returns a dictionary d of letters -> frequencies"""
     d = dict()
     for c in s:
          if c not in d:
               d[c] = 1
          else:
               d[c] += 1
     return d

print(scrabble_solver('laura'))
