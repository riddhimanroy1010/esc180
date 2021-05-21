def stringtime(str, n):
    return (str*n)

def front_times(str, n):
    if len(str) >= 3:
        return (str[:3]*n)
    else:
        return str*n
    
def string_bits(str):
    newstr = ""
    for i in range(len(str)):
        if i == 0 or i % 2 == 0:
            newstr += str[i]
    return newstr

def string_splosion(str):
    outstr = ""
    for i in range(len(str) + 1):
        outstr += str[:i]
    return outstr

def last2(str):
    last_sub_str = str[len(str) - 2: len(str)]
    counter = 0
    if str == "":
        return counter
    for i in range(len(str)):
        if str[i : i + 2] ==  last_sub_str:
            counter += 1
    return counter - 1

def array_count9(L):
    counter = 0
    for num in L:
        if num == 9:
            counter += 1
    return counter

def make_bricks(small, big, goal):
    for n in range(1, small):
        for m in range(1, big):
            if (n + 5*m) == goal:
                print((n + 5*m))
                print(goal)
                return True
    return False

def sum67(nums):
    sum = 0
    ignore = False
    for num in nums:
        if num == 6:
            ignore = True
        elif num == 7 and (ignore == True):
            ignore = False
        if not ignore:
            sum += 1
    return sum

def double_char(str):
    outstring = ""
    for char in str:
        outstring += 2*char
    return outstring

def count_hi(str):
    counter = 0
    for i in range(len(str)):
        if str[i : i + 2] == "hi":
            counter += 1
    return counter

def cat_dog(str):
    cat_count = 0
    dog_count = 0
    for i in range(len(str)):
        if str[i : i + 3] == "cat":
            cat_count += 1
        if str[i : i + 3] == "dog":
            dog_count += 1
    return cat_count == dog_count

def count_code(str):
    counter = 0
    for i in range(len(str)):
        if str[i : i + 2] == "co" and str[i + 3: i + 4] == "e":
            counter += 1
    return counter

def end_other(a, b):
    pass



if __name__ == "__main__":
    make_bricks(3, 1, 8)
    sum67([1, 2, 6, 8, 7])



