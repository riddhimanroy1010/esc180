#1
def power(x, n):
    '''
    n = 3
    x * power(x, 2) 
        n = 2
        x * power(x, 1)
            n = 1
            x
        x * x
    x * x * x
    '''
    if n == 1:
        return x

    return x * power(x, n - 1)

#2
final = []
def interleave(L1, L2):
    '''
    L1, L2
    len = 3
    interleave
        L1[1:], L2[1:]
        len = 2
        interleave
            L1[2:], L2[2:]
            len = 1
            interleave
                L1[2:], L2[2:]
    '''
    if len(L1) == 0:
        return []
    return [L1[0], L2[0]] + interleave(L1[1:], L2[1:])

print(interleave([1, 2, 3], [4, 5, 6]))

#3
def reverse_res(L, i=0):
    mid = (len(L) // 2)
    if len(L) == 1:
        return L
    if (mid - i >= 0) and (mid + i <= len(L)):
        if (len(L) % 2 != 0):
            L[mid - i], L[mid + i] = L[mid + i], L[mid - i]
        else:
            if i != 1:
                L[mid - i], L[mid + i - 1] = L[mid + i - 1], L[mid - i]
            else:
                pass
    else:
        return L
    reverse_res(L, i + 1)
    
L = [1, 2, 3, 4, 5, 6, 7]
reverse_res(L)
print(L)
L = [1, 2, 3, 4, 5, 6]
reverse_res(L)
print(L)
#4
def zigzag2(L, i = 0):
    mid = len(L)//2
    if len(L) == 0:
        print("")
    elif i == 0:
        print(L[mid], end = " ")
        zigzag2(L, i + 1)
    elif len(L) % 2 == 0:
        if (mid + 1 <= len(L)) and (mid - i >= 0):    
            print(L[mid + i], L[mid - i], end = " ")
            zigzag2(L, i + 1)
    else:
        if (mid + 1 <= len(L)) and (mid - i >= 0):    
            print(L[mid + i], L[mid - i], end = " ")
            zigzag2(L, i + 1)

zigzag2([1, 2, 3, 4, 5, 6, 7, 8, 9])



