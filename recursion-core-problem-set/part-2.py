# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    if not array:
        return False

    elif array[0] == query:
        return True
        
    return search(array[1:], query)



# is_palindrome
def is_palindrome(text):

    if len(text) == 0:
        return True
    
    elif text[:1] == text[-1]:
        return is_palindrome(text[1:-1])
        
    else:
        return False



# digit_match
def digit_match(alpha, omega):
    alpha = str(alpha)
    omega = str(omega)
    
    if not alpha or not omega:
        return 0
        
    elif alpha[-1] == omega[-1]:
        return 1 + digit_match(alpha[:-1], omega[:-1])
        
    else:
        return digit_match(alpha[:-1], omega[:-1])

