## Problem 1
def list1_start_with_list2(list1, list2):
    if len(list1) >= len(list2):
        same_len = True
    else:
        same_len = False
    for i in range(len(list2)):
        if list1[i] != list2[i]:
            same_element = False
        else:
            same_element = True
    if (same_len and same_element) == True:
        return True
    return False

## Problem 2
def match_pattern(list1, list2):
    len2 = len(list2) - 1
    for i in range(len(list1) - len(list2) + 1):
        if list1[i:i + len2 + 1] == list2:
            return True
    return False

## Problem 3
def repeats(list0):
    for i in range(len(list0)):
        if list0[i - 1] == list0[i]:
            return True
    return False

## Problem 4a
def print_matrix_dim(M):
    print(str(len(M)) + "x" + str(len(M[0])))

## Problem 4b
def mult_M_v(M, v):
    vector_v = []
    for i in range(len(v)):
        vector_v.append(v[i])
    for i in range(len(M)):
        for j in range(len(M[0])):
            M[i][j] *= vector_v[i]
    print(M)
    return M

## Problem 4c
def matrix_mult(M, N):
    res = []
    cur_vector_M = []
    cur_vector_N = []
    for i in range(len(M)):
        cur_vector_M = M[i]
        for j in range(len(N)):
            cur_vector_N.append(N[j][i])
            res[j] = 1
        print(cur_vector_M, cur_vector_N)
        cur_vector_N = []
    print(res)
    

## Testing ##
if __name__ == '__main__':
    print(list1_start_with_list2([1, 2, 3], [1, 2]))                #pass
    print(match_pattern([4, 10, 2, 3, 50, 100], [2, 3, 50]))        #fail
    print(repeats([1, 2, 2]))                                       #pass
    print_matrix_dim([[1,2],[3,4],[5,6]])                           #pass
    mult_M_v([[1, 2], [1, 2]], [1.0, 2.0])                              #pass
    #matrix_mult([[2, 4, 8], [1, 3, 6]], [[1, 9], [4, 6], [3, 7]])

