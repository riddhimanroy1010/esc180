## Moar lists
##Iterating over lists
L = [10, 2, 15, 20]

for i in range(len(L)): ##for loop over len of list
    print(L[i])

# Example where need to use for loop
def has_duplicates(L):
    '''Return true iff list L has duplicates'''
    for i in range(len(L)):
        if L[i] in L[(i + 1):len(L)]:
            return True
    return False

def has_duplicates2(L):
    Lsorted = sorted(L)
    for i in range(len(L) - 1):
        if Lsorted[i] == Lsorted[i + 1]:
            return True
    return False

##String lists
##Replacing characters
