''' Sorting '''
L = [1, 4, 2, 10, 89]
# Selection Sort (Max Sort)
# At interation i, find maximum element in L[:(n-i)] and put it in
# location L[n-i-1] (swap largest element with current element L[n - i - 1])
#iteration 0
#89 is largest, put at location L[n-i-1]
# L = [1, 4, 2, 10, 89]

#iteration 1
#10 is the largest element in L[:n - 1], put 10 in location L[n-1]

##repeat....

def max_i(L):
    '''Return index of largest element in L. If there is more than one 
    , return index of leftest one.'''
    cur_max = L[0]
    cur_max_i = 0

    for i in range(1, len(L)):
        if L[i] > cur_max:
            cur_max = L[i]
            cur_max_i = i
    return cur_max_i

def selection_sort(L):
    for j in range(len(L)):
        ind_of_max = max_i(L[ : len(L) - j])
        L[ind_of_max], L[len(L) - j - 1] = L[len(L) - j - 1], L[ind_of_max]

##Counting sort/ bucket sort
def counting_sort(L):
    max_L = max(L)
    counts = [0] * (max_L + 1)
    for e in L:
        counts[e] += 1
    
    res = []
    for elem in range(len(counts)):
        count = counts[elem]
        if count > 0:
            res.extend([elem] * count)
    return res

import random
##Bogo ssort
def is_sorted_nondecreasing(L):
    for i in range(len(L) - 1):
        if L[i] > L[i + 1]:
            return False
    return True

def bozosort(L):
    while not is_sorted_nondecreasing(L):
        i , j = int(len(L) * random.random()), int(len(L) * random.random())
        L[i], L[j] = L[j], L[i]
        print(L)
    return True

def fermat(p):
    n = 1
    while True:
        for i in range(1, n):
            for j in range(1, n):
                for k in range(1, n):
                    if i**p + j**p == k**p:
                        return i, j, k
                    else:
                        print(i**p + j**p, k**p)
        n += 1
    return False
if __name__ == "__main__":
    print(L)
    selection_sort(L)
    print(L)
    L = [1, 4, 2, 10, 89]
    print(L)
    counting_sort(L)
    print(L)
    L = [9,8,7,6,5,4,3,2,1,0]
    print(L)
    bozosort(L)
    print(L)
    #fermat(3)
    