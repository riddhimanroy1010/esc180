def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)

# time complexity
#1                                              1
#
#...                                       ....
#      (n - 2)(n - 3)       (n - 3)(n - 4)      
#            n - 1       n - 2                  
#                   n    
# We have fewer than 1 + 2 + 4 + 8... calls for n levels. Thus, this is 2^(n+1) - 1 calls
# In generally we have O(2^n) as upper bound
# Define T(n) as the runtime of fib(n)
# Thus, T(n) = fib(n) + fib(n-1) + fib(n-2)
# so T(n) ~ a*fib(n)
# so we can say that the worst runtime complexity of fib(n) is O(fib(n))
L1 = [[1, 2], [3, 4]]

def deep_copy(obj):
    '''
    return deep copy of list of lists of lists... of lists of integers
    '''

    #base case
    if type(obj) != list:
        return obj
    
    #recursive step
    copy = []
    for elem in obj:
        copy.append(deep_copy(elem))
    
    return copy
    