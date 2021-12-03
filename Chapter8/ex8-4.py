def any_lowercase(s):
     """ incorrect - only checks whether first letter is lower case"""
     for c in s:
          if c.islower():
               return True
          else:
               return False

def any_lowercase_fixed(s):
     for c in s:
          if c.islower():
               return True
     return False

          
def any_lowercase2(s):
     """ incorrect - checks if 'c' is lower case, which is
          always True, and returns a string not a Boolean"""
     for c in s:
          if 'c'.islower():
               return 'True'
          else:
               return 'False'

def any_lowercase3(s):
     """ incorrect - only returns the value of the final character of s"""
     for c in s:
          flag = c.islower()
     return flag

def any_lowercase4(s):
     """ correct """
     flag = False
     for c in s:
          flag = flag or c.islower()
     return flag

def any_lowercase5(s):
     """ incorrect - returns whether false if s contains any capital letters"""
     for c in s:
          if not c.islower():
               return False
     return True


          
