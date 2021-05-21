## Starter example: username and passwords ##
def login(username, password):
    global attempts
    if attempts >= 3:
        return "Refused, too many attempts"
    if username == "guerzhoy" and password == "hadjd":
        attempts = 0
        return "OK"
    elif username == "cluett" and password == "matrix":
        attempts = 0
        return "OK"
    elif username == "thywissen" and password == "newton":
        attempts = 0
        return "OK"
    else:
        attempts += 1
        return "Retry"

def initialize():
    global attempt
    attempt = 0

if __name__ == '__main__':
    login("cluett", "matrix")

## Lists ##
earnings = [91, 87, 115, 168] #syntax of a list or an array
print(len(earnings)) #length of array
print(earnings[1]) #indexing into the array
print(earnings[len(earnings) - 1]) #can use len to go from the other end

#lists can be iterated over
for i in range(len(earnings)):
    print("you will earn", earnings[i], "dollars a year")

for amt in earnings: #can index as entities in earnings, essentially letting the array decide the loop
    print(amt) #use this style unless you care about the location

def order(list):
    for i in range(len(list)):
        if list[i - 1] > list[i]:
            return False
    return True

#Lists can have different types of data
l = [1, 2, "hello"]
#lists of lists
L = [42, 43, [45, 46], 47]

#Example1
L = [[1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]]

for row in L: #row is a list in the list
    print(row)

#Modding lists
l = [0, 1]

l.insert(2, 99)#(element to insert before, element to insert)
l.insert(len(l), 99)

l.append("hi")#append is adding at the end of the list

l.index(1)#finding where an element it, returns the index of the first occurence of the element

2 in L #in operator returns if LHS in RHS

def check(lbound, ubound):
    n = lbound
    for i in range(0, ubound):
        l.append((2*i) + 1)
    for i in range(lbound, ubound):
        if n in l:
            odd.append(n)
        n += 1
    print(odd)

def initialize():
    global l, odd
    l = []
    odd = []

if __name__ == '__main__':
    initialize()
    check(5,10)











