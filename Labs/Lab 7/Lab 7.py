import numpy as np
def print_matrix(M_lol):
    ##return np.array(M_lol)
    pass

def get_lead_ind(row):
    for e in row:
        if e != 0:
            return row.index(e)

def row_to_swap(M, start_i):
    res = [0] * len(M)
    for i in range(start_i, len(M)):
        res[i] = get_lead_ind(M[i])
    res.remove(0)
    return res.index(min(res))

def add_rows_coefs(r1, c1, r2, c2):
    res_1 = [0] * len(r1)
    res_2 = [0] * len(r2)
    out = [0] * len(r1)
    for i in range(len(r1)):
        res_1[i] = c1 * r1[i]
    for i in range(len(r2)):
        res_2[i] = c2 * r2[i]
    for i in range(len(res_1)):
        out[i] = res_1[i] + res_2[i]
    return out

def eliminate(M, row_to_sub, best_lead_ind):
    for i in range(row_to_sub + 1, len(M)):
        r2 = M[i][best_lead_ind] / M[row_to_sub][best_lead_ind]
        if r2 == 1:
            continue
        M[i] = add_rows_coefs(M[row_to_sub], -r2, M[i], 1)

def backward_eliminate(M, row_to_sub, best_lead_ind):
    for i in range(row_to_sub  - 1, -1, -1):
        r2 = M[i][best_lead_ind] / M[row_to_sub][best_lead_ind]
        if r2 == 1:
            continue
        M[i] = add_rows_coefs(M[row_to_sub], -r2, M[i], 1)

def swapper(M, i):
    target_row = row_to_swap(M, i)
    M[0], M[target_row] = M[target_row], M[0]
    
def forward(M):
    for i in range(len(M)):
        swapper(M, i)
        eliminate(M, i, get_lead_ind(M[i]))

def backward(M):
    for i in range(len(M) - 1, -1, -1):
        backward_eliminate(M, i, get_lead_ind(M[i]))
    for i in range(len(M)):
        divisor = M[i][get_lead_ind(M[i])]
        for j in range(len(M[0])):
            M[i][j] /= divisor

def solve(M):
    res = []
    forward(M)
    print(np.array(M))
    #backward(M)
    print("RNF of Given Matrix")
    print(np.array(M))
    for i in range(min(len(M), len(M[0]))):
        b = M[i][len(M[i]) - 1]
        x = M[i][i]
        if x == 0 and x != b:
            print("No solution")
            return None
        elif (x and b) == 0:
            print("Infinite Solutions")
            return None
        res.append(b / x)
    for e in res:
        print("X" + str(res.index(e)), "=" , e)
    
    

M =[[ 0, 0, 1, 0, 2],
    [ 1, 0, 2, 3, 4],
    [ 3, 0, 4, 2, 1],
    [ 1, 0, 1, 1, 2]]

N = [[1, 1, 1, 2],
    [1, 2, 1, 3],
    [2, 3, 1, 5]]

forward(M)
