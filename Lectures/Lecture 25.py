'''Recursion'''

def fact(n):
    if n == 0:
        return 1

    return n * fact(n - 1)

def is_even(n):
    if n == 0:
        return True
    
    return not is_even(n - 1)

L = [1, 3, 9, 2, 10, 69, 420]

def print_list(L):
    '''print list element by element'''
    if len(L) == 0:
        return 
    
    print(L[0])
    print_list(L[1:])

print_list(L)

def is_win(n):
    '''Return true if being at sum n and having the turn results in a win'''
    #Base Case
    if n == 19 or n == 20:
        return True

    if (is_win(n + 1) and is_win(n + 2)) == False:
        return True
    
    return False


    

