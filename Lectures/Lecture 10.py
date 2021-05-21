## List Operations ##

##Slicing
L = [1, 2, 3, 4, 5, 6]
print(L[1:6:2]) #Start at element 1, go up to but not including element 6, in steps of 2
#L[Start:endnotinclusive:step]

print(L[1: :2]) #if have nothing in second argument, then no end. If have nothing in third argument, then default step is 1.

print(L[4: :-1]) #start at 4, then go backwards by 1

print(L[ : :-1]) #start at end, then go back by 1

print(L[ : :1]) #start at end, then go back by 1

''' default for slicing: [0:last:step], if step > 0, default step = 1.
    [0:last:step] if step > 0
'''
L[len(L) - 1: len(L) - 4: -1] ##from -1th element, to -4th element then step by -1
L[-1:-4:-1] #same as above

def manual_slice(L, i, j, step):
    ''' return L[i:j:step] without using slicing '''
    res = []
    for n in range(i, j, step):
        res.append(L[n])

    return res

def manual_slice_while(L, i, j, step):
    '''same thing as manual slice except use while'''
    res = []
    while i < j:
        res.append(L[i])
        i += step
    return res

def manual_slice_while_neg(L, i, j, step):
    '''now accounting for i and j and step < 0'''
    res = []
    if step > 0:
        while i < j:
            res.append(L[i])
            i += step
    elif step < 0:
        while i > j:
            res.append(L[i])
            i += step
    else:
        print("Invalid")
    return res

## Extensions
''' extensions take elements from one list (or given) and adds them to another list.
    NOT SAME AS ADD'''
L = [1, 2, 3]
M = [4, 5, 6]
L.extend(M) #L = [1, 2, 3, 4, 5, 6]
print(L)
L = [1, 2, 3]
M = [4, 5, 6]
L.append(M) #L = [1, 2, 3, [4, 5, 6]] append slaps the whole list as an element, extend makes them into elements in another list.
print(L)

if __name__ == '__main__':
    print(manual_slice([1,2,3], 1, 2, 1))
    print(manual_slice_while([1,2,3], 1, 2, 1))
    print(manual_slice_while_neg([1,2,3], 1, 2, 1))


