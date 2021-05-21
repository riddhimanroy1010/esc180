#1a
def insert(L, e):
    L.append(e)
    return sorted(L)

print(insert([3.0, 4.0, 5.0], 3.5))

#runtime complexity: O(nlogn) since python presumably uses merge sort

#2
def select_gifts(good_ratings, want_ratings):
    for k, v in good_ratings.items():
        if k not in want_ratings:
            want_ratings[k] = 0
            good_ratings[k] = 0
    for k,v in want_ratings.items():
        if k not in good_ratings:
            want_ratings[k] = 0
            good_ratings[k] = 0   
    good_ratings = sorted(good_ratings, key = good_ratings.get, reverse= True)
    want_ratings = sorted(want_ratings, key = want_ratings.get, reverse= True)
    return [good_ratings[0], want_ratings[0]]

good_ratings = {"Calc textbook": 5, "iPhone": 1, "Alarm clock": 4, "Notebooks": 4}
want_ratings = {"iPhone": 4, "A+ in CSC": 5, "Calc textbook": 4, "Notebooks": 5}
print(select_gifts(good_ratings, want_ratings))

#3
def transpose(M):
    ''' 
    transpose a matrix
    for example: M =  [[5, 6, 7], [0, -3, 5]].
    return
    M = [5, 0], [6, -3], [7, 5]
    '''
    out = []
    k = 0
    while k < len(M[0]):
        temp = []
        for i in range(len(M)):
            temp.append(M[i][k])
        out.append(temp)
        k += 1
    
    return out

print(transpose([[5, 6, 7], [0, -3, 5]]))

#q4
def max_rec(l):
   
    if len(l) == 1:
        return l[0]
    
    res = max_rec(l[1:])

    if res > l[0]:
        return res
    else:
        return l[0]



print(max_rec([103, 180, 101, 102, 180, 420]))
        

#q5
def is_fib(L):
    size = len(L)
    if L == []:
        return True
    if size == 1 and (L[0] == 1):
        return True
    if size == 2 and (L[0] == 1 and L[1] == 1):
        return True
    
    return L[-1] == L[-2] + L[-3] and is_fib(L[0 : -1])

print(is_fib([1, 1, 2, 3, 4]))


#q7
'''
1. O(n^2)
2. O(n^2)
3. each call generates 2 new calls to itself. O(2^n)
4. O(1)
'''

#q9
def sorted_timestamps(timestamps):
    out = [0]*len(timestamps)
    new_out = []
    for i in range(len(timestamps)): #O(n)
        out[i] = timestamps[i][0]*60 + timestamps[i][1]

    out = sorted(out)
    for i in range(len(out)):
        new_out.append((out[i] //60, out[i] % 60))
    
    return new_out

print(sorted_timestamps([(5, 10), (2, 40), (22, 59), (5, 10)]))

#q10
friends = {"Carl Gauss": ["Isaac Newton", "Gottfried Leibniz", "Charles Babbage", "Ada Lovelace"],
            "Gottfried Leibniz": ["Carl Gauss"],
            "Isaac Newton": ["Carl Gauss", "Charles Babbage"],
            "Ada Lovelace": ["Charles Babbage", "Michael Faraday", "Carl Gauss"],
            "Charles Babbage": ["Isaac Newton", "Carl Gauss", "Ada Lovelace"],
            "Michael Faraday" : ["Ada Lovelace"]}
        
#Approach 1: Make all friend lists sets including the person whose friends they are, then do intersections to find common ones.
def set_maker(n):
    out = []
    for i in range(n):
        new_set = set()
        out.append(new_set)
    return out


def max_clique(friends):
    set_list = set_maker(len(friends))
    i = 0
    for k, v in friends.items():
        cur_list = v
        cur_list.append(k)
        set_list[i] = cur_list
        i += 1
    
    length = 0
    for i in range(len(set_list)):
        if len(set_list[i]) > length:
            length = len(set_list[i])
    
    pass


        
print(max_clique(friends))

            