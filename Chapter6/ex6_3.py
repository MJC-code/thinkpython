def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def is_palindrome(s):
    if len(s) == 0 or len(s) == 1:
        return True
    elif first(s) != last(s):
        return False
    else:
        print ('calling is_palindrome on', middle(s))
        return is_palindrome(middle(s))

    
