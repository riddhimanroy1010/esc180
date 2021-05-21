''' More loop work '''
L = [4, 5, 6]
for e in L:
    L.append(e)
    input("Press any key \n") ##ask user input
    print(L)

##removing entries from a list
L = [1.0, 2.0, 3.0, 4.0]
for i in range(len(L)):
    if L[i] == 4.0:
        del L[i]
##^^ Will return an error because post deletion there is no more L[3]
##and so results in an error for out of range

L = [1.0, 2.0, 3.0, 4.0, 4.0]
i = 0
while i < len(L):
    if L[i] == 4.0:
        del L[i]
    else:
        i += 1
    
''' Dictionaries '''
grades = {"PHY" :90, "CIV" : 100, "PRA" : 69, "CSC" : "TBD"}
##Keys have to be immutable, meaning they cannot be modified.
for key in grades:
    print(key)
    print(grades[key])

grades["MAT"] = 0

list(grades.keys())
list(grades.values())

for key in grades:
    print(key, grades[key])

list(grades.items())[0][1]

''' Tuples '''
##Like lists, but immutable

a = (4, 5, 6)

a[0]

for elem in a:
    print(elem)

grades[("aaa", "bbb")] = "hi"

grades = {"PHY" :90, "CIV" : 100, "PRA" : 69, "CSC" : "TBD"}

for key, value in grades.items():
    print(key, value)

a = (4, 5, 6)

four, five, six = a #unpacking a tuple

''' Uses of dicts '''
gradebook = {"PHY" : "A", "PRA" : "A-", "CALC" : "A"}

def get_subj(grades, target_grade):
    subjects = []
    for subj, grade in gradebook.items():
        if grade == target_grade:
            subjects.append(subj)
    return subjects

##Inverting a dict: make a new dict whose keys are the values of the input
##dict and whose values are the lists of the keys of the old dict

def invert_grades(grades):
    inverted_grades = {}
    all_grades = list(grades.values())
    for grade in all_grades:
        inverted_grades[grade] = get_subj(grades, grade)
    return inverted_grades

def invert_grades2(grades):
    inverted_grades = {}
    for grade in grades.values():
        inverted_grades[grade] = get_subj(grades, grade)
    return inverted_grades





