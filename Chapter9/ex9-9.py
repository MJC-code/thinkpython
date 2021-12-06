
def car_talk3():
     """Finds and prints palindromic ages for 2 people with age difference
        ranging from 1 to 100
        Assumes birthdays are on the same day!
        Answer to the question is son is 57, mum is 75"""
     for age_difference in range(1, 99):
          counter = 0
          ages = ''
          for son_age in range (1, 99):
               mum_age = son_age + age_difference
               fill_length = len(str(mum_age))
               s = str(son_age).zfill(fill_length)
               m = str(mum_age).zfill(fill_length)
               if is_reverse(s, m):
                    counter = counter + 1
                    ages = ages + s + '   ' + m + '\n'
          if counter == 8:
               print ('This age difference is', age_difference, '\nThe current age of the son is the sixth value below')
               print('Son  Mum')
               print(ages)
               
def is_reverse(word1, word2):
     return word1[:] == word2[::-1]


car_talk3()




