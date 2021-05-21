''' Matrix Work '''
a = [[1, 0, 0, 2],
    [0, 0, 0, 5]]

sparse_a = {(0,0) : 1, (0, 3): 2, (1, 3): 5}

def sparce_mat_to_mat(sparce, dims):
    mat = []
    for row in range(dims[0]):
        mat.append([0] * dims[1])

    for coord, value in sparce.items():
        mat[coord[0]][coord[1]] = value
    
    return mat

def mult_sparce_by_vec(sparce, vec, m):

    out = [0] * m

    for coord, value in sparce.items():
        out[coord[0]] += value * vec[coord[1]]
    return out

''' Files '''

