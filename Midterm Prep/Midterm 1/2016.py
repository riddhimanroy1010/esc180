''' Problem 1a '''
def halloween_reaction(thing):
    banned_words = ["ghost", "monster", "midterm"]
    if thing in banned_words:
        return "NOO!"
    return "YAY!"

''' Problem 1b '''
def print_mid_part(L):
    for i in range (1, len(L) - 1):
        print(L[i])

''' Problem 1c '''
def h(L):
    L[0] = "fall"
    L[1] = "colours"

''' Problem 2a '''
def odd_sums(L):
    sum = 0
    for i in range(len(L)):
        if L[i] % 2 != 0:
            sum += L[i]
    return sum

''' Problem 2b '''
#for i range(5, 500, 3):
    #print(i)
def loop_convert():
    i = 5
    while i < 500:
        print(i)
        i += 3
    
''' Problem 3a '''
def kids_who_like_candy(faves, kids):
    candy_kids = []
    for i in range(len(faves)):
        if faves[i] == "candy":
            candy_kids.append(kids[i])
    return candy_kids

''' Problem 3b '''
def cube_root(n):
    cube = False
    num = 1
    while cube == False:
        if (num * num * num) == n:
            cube = True
            break
        num += 1
    return num

''' Problem 4 '''
countdown = 4
def halloween_surprise():
    global countdown
    countdown -= 1
    if countdown > 0:
        return countdown
    else:
        return "SURPRISE!"

''' Problem 6 '''
def has_single_peak(L):
    peak = max(L)
    peak_index = 0

    #Locating the peak
    for i in range(len(L)):
        if L[i] == peak:
            peak_index = i

    for i in range(len(L) - 1):
        #to the left of peak (increasing side)
        if i < peak_index:
            if L[i + 1] < L[i]:
                return False
        #to the right of peak (decreasing side)
        if i > peak_index:
            if L[i + 1] > L[i]:
                return False
    return True

''' Problem 7 '''
def max_arrivals_2hrs(arrivals):
    kid_count = 0
    for i in range(len(arrivals)):
        if arrivals[i] <= 120:
            kid_count += 1
    return kid_count
    
''' testing '''
if __name__ == "__main__":
    print(halloween_reaction("ghost"))
    print_mid_part(["pumpkins", "candy", "costumes", "autumn", "zombies"])
    L = ["tricks", "treats"]
    h(L)
    print(L) #should print ["fall", "colours"]
    x = "Spice"
    y = "Pumpkin"
    x += x
    print(y+x, "Latte")
    print(odd_sums([1, 3, 4, 5],))
    print(kids_who_like_candy((["candy", "costumes", "weather", "candy"]), (["Bob", "Dorothy", "Mike", "Alice"])))
    print(cube_root(27))
    print(halloween_surprise()) #Output: 3
    print(halloween_surprise()) #Output: 2
    print(halloween_surprise()) #Output: 1
    print(halloween_surprise()) #Output: SURPRISE!
    print(has_single_peak([3, 2, 1] ))
    print(max_arrivals_2hrs([0, 30, 40, 150, 160, 170, 370]))
