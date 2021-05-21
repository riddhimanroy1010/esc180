#Set
s1 = {131, 2, 23, 4} #can contain any object, unordered

s2 = {"hi", 5}

L1 = list(s1) #converting a set to a list
set(L1) #removes redundant elements

a = {1, 2, 3}
b = {1, 3, 5}
final = a.intersection(b)
final2 = a.union(b)

print(final, final2)

d = {1:2, 3:4}
k = 5
if k in d:
    print(d[k])
else:
    print("key not in dict")

def manual_get(d, k, default):
    if k in d:
        return d[k]
    else:
        return default

to_add = {5:6, 7:8} #updating dicts
d.update(to_add)

def manual_update(d, to_add):
    for k, v in to_add.items():
        d[k] = v


# Merge Sort
def merge_sort(L):
    mid = len(L)//2
    sorted1 = merge_sort(L[:mid])
    sorted2 = merge_sort(L[mid:])
    return merge_sort(sorted1, sorted2)