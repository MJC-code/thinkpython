def rotate_word(word, n):
     """Rotates each letter of the word by n letters"""
     answer = ''
     for letter in word:
          letter = rotate_letter(letter, n)
          answer = answer + letter
     print(answer)     
          



def rotate_letter(letter, n):
     """Rotates a letter of the alphabet by n letters"""
     if 65 > ord(letter) < 122:
          return letter

     if letter.islower():
          new_letter = letter.upper()
     else:
          new_letter = letter

     numeric_rep = ord(new_letter) - 65
     numeric_rep = (numeric_rep + n) % 26
     numeric_rep = numeric_rep + 65

     if letter.islower():
          return chr(numeric_rep).lower()
     else:
          return chr(numeric_rep)



     
          

