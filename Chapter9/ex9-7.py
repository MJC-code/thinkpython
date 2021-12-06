
def car_talk1():
     """Finds words that contain 3 consecutive double letters"""
     fin = open('words.txt')
     
     for line in fin:
          word = line.strip()
          if consecutive_3_double(word):
               print(word)


def consecutive_3_double(word):
     """Checks word for 3 consecutive double letters. Return Boolean"""
     for i in range(len(word)-5):
          if word[i] == word[i+1]:
               if word[i+2] == word[i+3]:
                    if word[i+4] == word[i+5]:
                         return True
     return False


car_talk1()
          





