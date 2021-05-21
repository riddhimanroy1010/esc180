''' Problem 1a '''
def wish_happy_holiday(holiday_name):
    out = ("Happy" , holiday_name + "!")
    return out

''' Problem 1b '''
def print_first_half(L):
    iter = len(L)//2
    for i in range(iter):
        print(L[i])

''' Problem 1c '''
def h():
    global trick, treat
    treat = "treat"
    trick = "trick"
    return treat

''' Problem 2a '''
def count_engineers(costumes):
    counter = 0
    for i in range(len(costumes)):
        if costumes[i] == "engineer":
            counter += 1
    return counter

''' Problem 2b '''
def factorize(n):
    trial = 2
    factored = False
    while factored == False:
        if n % trial == 0:
            factored = True
            break
        else:
            trial += 1
    return trial

''' Problem 2c '''
def switch_columns(M, i, j):
    for s in range(len(M)):
        for a in range(len(M[0])):
            initial_i_element = M[s][i]
            initial_j_element = M[s][j]
            M[s][i] = initial_j_element
            M[s][j] = initial_i_element 
    return M

''' Problem 4 '''
def is_symmetric(L):
    centerpoint = len(L)//2
    if len(L) % 2 == 0: #even sized list, midpoint technically dne, so halves of list to comp
        print(L[:centerpoint])
        print(L[centerpoint:])
        if L[:centerpoint] == L[-1:centerpoint - 1]:
            return True
    else:
        return False
    return False



''' testing '''
if __name__ == "__main__":
    print(wish_happy_holiday("Halloween"))
    print_first_half(["pumpkins", "candy", "costumes", "autumn"])
    trick = "midterm"
    treat = "exam"
    treat = h()
    print(trick + " or " + treat) #should print "trick or treat"
    print(count_engineers(["engineer", "doctor", "firefighter", "engineer", "pirate", "artsie"]))
    print(factorize(272483))
    M = [[5, 6, 7],
    [0, -3, 5]]
    print(switch_columns(M, 0, 1))
    print(is_symmetric(([1, 2, 2, 1])))