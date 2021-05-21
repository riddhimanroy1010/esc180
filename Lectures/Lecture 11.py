## More Lists ##

##Sorting
L = ["PHY", "ESC", "CIV"]

M = sorted(L) #returns a new list that is the previous one sorted

L.sort() #modifies L and replaces it as the sorted version

sorted(L, reverse = True) #sorts from descending order

##Splicing
L = [1, 2, 3, 4, 5]

L[1:3] = [10, 11, 12] #replaces that splice with this value

## Example: Estimating Pi ##
''' Monty Python Simulation
P(inside quarter circle)/P(inside unit circle square) = pi/4'''

import random

pts_inside = 0
N = 10000000
for i in range(N):
    x, y = random.random(), random.random()
    if x**2 + y**2 < 1:
        pts_inside += 1

pi_approx = 4 * pts_inside / N
