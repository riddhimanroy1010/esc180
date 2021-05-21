L1 = [1, 2, 3]

# Aliasing
L2 = L1

L1[0] = 2

# L2 is an alias of L1


# Copy
L1 = [1, 2, 3]
L2 = [1, 2, 3]

L1[0] = 2
L1
L2
###############################

L1 = [1, 2, 3]
L2 = [L1[0], L1[1], L1[2]]


L1 = [1, 2, 3]
L1[:]

# make a function that creates a non-aliased copy of the list L1,
# (a list of integers)
# which is stored as a global variable

def make_copy():
    L2 = []
    for e in L1:         # for i in range(len(L1)): L2.append(L1[i]))
        L2.append(e)
    return L2

L1 = [1, 2, 3]
L2_copy = make_copy()
# L2_copy has to be [1, 2, 3]
L1[0] = 2
# L2_copy has to be [1, 2, 3]


def copy_list_ints(L1):
    '''Return a copy of the list of integers L1'''
    L2 = []
    for e in L1:
        L2.append(e)
    return L2


L1 = [3, 4, 5]
L2 = copy_list_ints(L1)




L2 = L1[:]   # L1[:] is shorthand for [L1[0], L1[1], .... L1[len(L1)-1]]
L2 = L1.copy()

# Copy with slicing

# (aside on *)
L = [[0] * 5] * 2
L = []
for i in range(2):
    L.append([0] * 5)

# Shallow copy
L1 = [[1, 2], [3, 4]]
L2 = []
for e in L1:
    L2.append(e)
# same as L2 = L1.copy() or L2 = L1[:]

# e = L1[0]
# L2.append(e)

L1[0] = 42

# Manual deep copy
L1 = [[1, 2], [3, 4]]
L2 = []
for e in L1:
    elem_list = []
    for i in e:
        elem_list.append(i)
    L2.append(elem_list)


# shorter version of deep copy

L1 =  [[1, 2], [3, 4]]
L2 = []
for sublist in L1:
    L2.append(sublist[:])


# deep copy of a list of lists

L1 = [[[1, 2]], [[3, 4]]]
L2 = []
for sublist in L1:
    L2.append(sublist[:])



# reverse strings
# anagrams


# a router needs to receive  N  data packets (represent them as strings), and needs to transmit one of the  N  packets, uniformly at random (i.e., each packet should have an equal probability of being transmitted.