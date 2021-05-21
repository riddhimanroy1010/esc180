''' Problem 1a '''
def happyhallo():
    print("Happy Halloween")

if __name__ == "__main__":
    happyhallo()

''' Problem 1b '''
def print_almost_all(L):
    print(L[:len(L) - 1])

''' Problem 1c '''
def h():
    global treat
    treat = "candy"
    return treat

if __name__ == "__main__":
    treat = "pumpkin"
    h()
    print(treat)

''' Problem 2b '''
def print_range():
    n = -500
    while n <= 500:
        print(n)
        n += 1

''' Problem 2d '''
def all_not_same(a, b, c):
    if (a != b) or (b != c):
        return False
    return True

''' Problem 4 '''
def flatten(list_of_lists):
    '''Return a new list that contains every value in each of the sub-lists of
    list_of_lists. For example,
    >>> flatten([[1, 3], [’a’, ’b’, ’c’]])
    [1, 3, ’a’, ’b’, ’c’]
    Assume that all the elements of list_of_lists are lists and that the elements
    of the elements of list_of_lists are integers or strings.'''
    out_list = []
    for i in range(len(list_of_lists)):
        for elements in list_of_lists[i]:
            out_list.append(elements)
    return out_list

def all_possible_combos_less_2_repeats():
    out_list = []
    alpha_set = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    for alpha1 in alpha_set:
        for alpha2 in alpha_set:
            for alpha3 in alpha_set:
                for alpha4 in alpha_set:
                    if not ((alpha1 == alpha2  == alpha3) or (alpha2 == alpha3 == alpha4) or
                    (alpha1 == alpha3 == alpha4) or (alpha1 == alpha2 == alpha4)):
                        out_list.append(alpha1 + alpha2 + alpha3 + alpha4)
    print(out_list)

    
