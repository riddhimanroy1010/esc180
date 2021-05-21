
# Merge Sort

def merge_broken(L1, L2):
    '''Return the sorted version of L1 + L2'''
    ''' IMPERFECT VERSION '''
    out = []
    if len(L1) == len(L2):
        for i in range(len(L1)):
            out.append(min(L1[i], L2[i]))
            out.append(max(L1[i], L2[i]))
    elif len(L1) > len(L2):
        for i in range(len(L2)):
            out.append(min(L1[i], L2[i]))
            out.append(max(L1[i], L2[i]))
        leftover = len(L1) - len(L2)
        out.append(L1[len(L1) : leftover: -1])
    elif len(L1) < len(L2):
        for i in range(len(L1)):
            out.append(min(L1[i], L2[i]))
            out.append(max(L1[i], L2[i]))
        leftover = len(L1) - len(L2)
        out.append(L2[len(L2) : leftover: -1])
    return out

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

def merge_sort(L):

    if len(L) <= 1:
        return L[:]

    mid = len(L)//2
    sorted1 = merge_sort(L[:mid])
    sorted2 = merge_sort(L[mid:])
    return merge(sorted1, sorted2)

print(merge([1, 3, 5, 9], [2, 4, 7]))


# [1] [1] [1]....                   [1]
#   .......
#   [n/4]   [n/4]   [n/4]   [n/4]
#          [n/2]    [n/2]
#               [n]
#
# How many calls to merge_sort? 1 + 2 + 4...2^n calls; sum = O(2log(2n))
# To merge? Total levels = log(2n) + 1; for length n, takes k seconds. So total complexity is nlog(n) calls
#

'''
Comparision based sort algorithms

Deicions about how to arrange the sorted version of the list are based on
code in the format:
if L[i] < L[i]:
    ...
else:
    ...

In total, for a given length, we have n! possible solutions of sorting list L
if statement #1: narrowing it down from n! to n!/2
             #2: n!/4...

need total log2(n!) if statements to narrow down the space of possible solutions to 1
stirlings approximation: log2(n!) = O(nlog(n))
'''