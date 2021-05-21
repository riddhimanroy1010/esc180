#1
def most_productive_elf(toys_produced):
    return sorted(toys_produced, key = toys_produced.get, reverse= True)[0]

toys0 = {"Bob":4000, "Gloria":7000, "Hugo":10000, "Grumbles":42}


#2
def two_smallest(L):
    return [sorted(L)[1], sorted(L)[0]] #O(nlogn) presuming quick sort by python

#3
def largest_col_sum(M):
    out = []
    k = 0
    while k < len(M[0]):
        sum = 0
        for i in range(len(M)):
            sum += M[i][k]
        out.append(sum)
        k += 1
    return max(out)

#6
def filter_out_odds(L):
    if L == []:
        return L
    if L[0] % 2 == 0:
        return [L[0]] + filter_out_odds(L[1 :])
    else:
        return filter_out_odds(L[1: ])
#8
def ev(expr):
    pass
