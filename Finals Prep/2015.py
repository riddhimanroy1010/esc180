#1
def is_sorted(L):
    if L == sorted(L) or L == (sorted(L, reverse=True)):
        return True
    return False

#2
def euc_distance(u, v):
    #blank list initialization
    vec1 = [0]*(max(u.keys()))
    vec2 = [0]*(max(v.keys()))

    #ensuring same lengths
    if len(vec1) < len(vec2):
        while len(vec1) != len(vec2):
            vec1.append(0)
    elif len(vec1) > len(vec2):
        while len(vec1) != len(vec2):
            vec2.append(0)
    #getting the sparse array
    for keys, values in u.items():
        vec1[keys - 1] = values
    for keys, values in v.items():
        vec2[keys - 1] = values
    #distance formula
    dist = 0
    for i in range(len(vec1)):
        dist += (vec1[i] - vec2[i])**2
    
    return dist**(1/2)
    
#q3
def movies_by_release_date(movies):
    T = -100000
    final_out = {}
    for k, v in movies.items():
        if "a long time ago" in v:
            final_out[k] = T
        else:
            final_out[k] = int(v[ : 4])
        
    final_out = sorted(final_out, key = final_out.get, reverse= True)
    return final_out

#4
def merge(L1, L2):
    if len(L1) == 0:
        return L2 
    if len(L2) == 0:
        return L1 
    if L1[0] < L2[0]:
        return [L1[0]] + merge(L1[1:], L2)
    if L2[0] < L1[0]:
        return [L2[0]] + merge(L1, L2[1: ])


if __name__ == "__main__":
    u = {1:4, 2:5, 4:10}
    v = {1:5, 2:4, 3:10, 4:20}
    print(euc_distance(u, v))
    movies = {"Dude, Where’s My Death Star": "a long time ago, in a galaxy far far away",
            "Star Wars: The Force Awakens": "2015, in Los Angeles",
            "Star Wars": "1977, in Los Angeles",
            "Sleepless in Aldera": "a long time ago, in Alderaan City",
            "Jurassic World": "2015, in New York"}
    print(movies_by_release_date(movies))
    print(merge([4, 8, 10], [2, 5, 7]))