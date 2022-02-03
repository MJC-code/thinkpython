def find(word, letter, start):
     """Searches word for letter, starting at index start,
          returns index of first hit or -1 if letter not found"""
     index = start
     while index < len(word):
          if word[index] == letter:
               return index
          index = index + 1
     return -1

def count(word, letter):
     count = 0
     for c in word:
          if c == letter:
               count = count + 1
     print(count)

def revised_count(word, letter):
     count = 0
     index = 0
     while True:
          result = find(word, letter, index)
          if result == -1:
               return count
          count = count + 1
          index = result + 1
          
          
