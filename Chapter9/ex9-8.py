
def car_talk():
     """Searches 6 digit numbers from 000000 to 999999 for those where
          number : last 4 digits are palindromic
          number + 1: last 5 digits are palindromic
          number + 2: all 6 digits are palindromic"""
     for i in range(0, 999999):
          j = str(i).zfill(6)
          if is_palindrome(j[2:]):
               k = str(i+1).zfill(6)
               if is_palindrome(k[1:]):
                    l = str(i+2).zfill(6)
                    if is_palindrome(l):
                         print(j)
          


def is_palindrome(word):
     return is_reverse(word, word)


def is_reverse(word1, word2):
     if len(word1) != len(word2):
          return False
     i = 0
     j = len(word2) - 1
     while j >= 0:
          if word1[i] != word2[j]:
               return False
          i += 1
          j -= 1
     return True


car_talk()



