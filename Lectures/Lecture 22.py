''' Complexity '''
def longest_run1(s, c):
    run = 0
    max_run = 0

    if c == "z":
        s += "y"
    else:
        s += "z"

    for ch in s:
        if ch != c:
            max_run = max(max_run, run)
            run = 0
        else:
            run += 1
        
    return max_run
##Runtime complexity dependant on the length of s, therefore O(len(s))
##O(n)

def longest_run2(s, ch):
    for longest in range(len(s), -1, -1):
        if ch*longest in s:
            return longest
    return 0
def longest_run22(s, ch):
    for longest in range(len(s), -1, -1):
        cur_run = 0
        for i in range(len(s)):
            if s[i] == ch:
                cur_run += 1
            else:
                cur_run = 0
            if cur_run == longest:
                return longest
    return 0

''' Run times '''
def apply_it(f, arg1):
    return f(arg1)
    
def g(n):
    return n + 2

def f(n):
    for i in range(n):
        pass

import time

def time_it1(f, arg1):
    t1 = time.time()
    f(arg1)
    t2 = time.time()
    return t2 - t1

def time_it2(f, arg1, arg2):
    t1 = time.time()
    f(arg1, arg2)
    t2 = time.time()
    return t2 - t1

times = []
s_lengths = []
for s_length in range(10, 10000, 1000):
    s = s_length*"a" + "b"
    c = "z"
    times.append(time_it2(longest_run22, s, c))
    print(s_length, times)
    s_lengths.append(s_length)

import matplotlib.pyplot as plt
plt.plot(s_lengths, times)
plt.show()
