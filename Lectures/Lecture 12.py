## Infinite Loops ##
while True:
    print("Praxis")

##breaking
i = 0
while i < 100:
    if i == 1:
        print("Hello there")
    if i == 2:
        print("General Kenobi")
    if i > 2:
        print("*deploys sword#" + str(i) +"*")
    i += 1
L = [1, 3, 2]
def missing_k(L):
    L = sorted(L)
    for i in range(1, len(L) + 1):
        if i not in L:
            return i

