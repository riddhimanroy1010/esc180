'''Return to merge sort'''
def merge(L1, L2):
    i1 = 0
    i2 = 0
    res = []
    while i1 < len(L1) and i2 < len(L2):
        if L1[i1] < L2[i2]:
            res.append(L1[i1])
            i1 += 1
        else:
            res.append(L2[i2])
            i2 += 1
    res.extend(L1[i1:])
    res.extend(L2[i2:])
    return res

def insertion_sort(L):

    if len(L) <= 1:
        return L[:]

    mid = 1
    sorted1 = insertion_sort(L[:mid])
    sorted2 = insertion_sort(L[mid:])
    return merge(sorted1, sorted2)

#               [1]                 k*n
#       [n - 1]                     k*(n - 1)
#   [n - 2]                         k*(n - 2)
#  [n - 3]                          k*(n - 3)
# ...
# [1]                               k
#   Total runtime = k*(n + n - 1 + n - 2.... + 1) = n + n + n....kn(n+1)/2 = O(n^2)

''' Different kinds of call trees '''
# Factorial
#       Only one recursive call from each call, runtime does not depend on n, n decreases linearly
# total calls = n + 1

# Exponentiation
#   Only one recursive call from each call, runtime does not depend on n, n decreased by a constant factor
# total calls: nlog(n)

# Slow
#     Two recursive calls, runtime does not depend on n, n decreases by 1 each time
# Count by levels: level 1: 1, level 2: 2, level 3: 8....level n: 2^(n) calls
# sum of geometric series: 2^(n + 1) - 1 / (2 - 1)

# Sum List
#       Two recursive calls, runtime does not depend on n, n decreases by constant factor each time
# 1 + 2 + 4 + 8...n; let 2^k = n;
# runtime = 2(k + 1) - 1; k = log2(n)
# therefore runtime = 2(log2(n) + 1); O(log(n)

# Mergesort
#       Two recursive calls, runtime DOES depend on n, n decreases by 1 each time
