# Print all strings of length n over alphabet

def print_all(alphabet, n, start_str = ""):
    ''' 
    print all strings over alphabet alphabet of length n
    pre-pend the string start_str to the start of every str
    '''
    if n == 0:
        print(start_str)
        return None
    
    for letter in alphabet:
        print_all(alphabet, n - 1, start_str + letter)

print_all("abcd", 3, "z")

''' Runtime complexity
    1. Each loop does the same amount of work in k seconds.
    2. How many calls?
        k = len(alphabet)
        first level: k calls
        2: k^2 calls
        3: k^3 calls
        n: k^n calls
        Sum: (k^(n + 1) - 1/(k - 1)) ~ k^n calls
    Therefore, O(k^n) complexity
'''

def all_combinations(alphabet, n, start_str = ""):

    if n == 0:
        return [start_str]

    out = []
    for letter in alphabet:
        out.extend(all_combinations(alphabet, n - 1, start_str + letter))
    
    return out


print(all_combinations("abcd", 6, "z"))

''' 2016 exam question'''
def get_all_subsets(L):

    if len(L) == 0:
        return [[]]
    
    all0 = get_all_subsets(L[1:])
    res = []
    for subset in all0:
        res.append((L[0]) + subset)
    res.extend(all0)
    return res

'''
[] -> [[]]
|
[3] -> [[], [3]]
|
[2, 3] -> [[2], [2, 3], [], [3]]
|
[1, 2, 3] -> [[1, 2], [1, 2, 3], [1], [1, 3], [2], [2, 3], [], [3]]
'''





    