def scrabble_solver(rack_letters):
     word_list = {}
     result = []
     rack_letters = histogram(rack_letters)
     fin = open('words.txt')   
     for word in fin:
          word_list[word] = histogram(word.strip())

#     for i in word_list:
#          print(i, word_list[i])
     for word in word_list:
          for letter in word_list[word]:
               print(word[letter])
          
         
                


     return result
          
          

def histogram(s):
     """Takes a string s, returns a dictionary d of letters -> frequencies"""
     d = dict()
     for c in s:
          if c not in d:
               d[c] = 1
          else:
               d[c] += 1
     return d

print(scrabble_solver('aa'))

