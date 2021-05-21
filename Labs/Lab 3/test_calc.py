## Problem 1 ##
import lab02

if __name__ == '__main__':
    lab02.initialize()
    lab02.add(5)
    lab02.multiply(10)
    lab02.display_current_value()

    if lab02.get_current_value() == 50:
        print("1 pass")
    else:
        print("1 fail")

## Problem 2 ##
''' sum of cubes: implement summation for divergent series of cubes'''
def self_cubicsum(n):
    total = 0
    for i in range (1, n + 1):
        total += i**3
    print(total)

def formula_cubicsum(n):
    ''' from reference site:
    the sum of n consecutive cubes = square of the first n numbers'''
    total = (n**2)*((n + 1)**2)*(1/4)
    print(total)

def check_sum(n):
    if self_cubicsum(n) == check_sum(n):
        return True
    return False

def check_sums_up_to_n(N):
    for i in range(N + 1):
        if self_cubicsum(i) != formula_cubicsum(i):
            return False
    return True

## Problem 3 ##
''' implementing the leibniz approximation for pi'''
import math
def leibniz_pi_approx(n):
    ''' n is degree of approximation.
    Formula: sum from 0 until n (-1)**n/(2n+1)'''
    total = 0
    for i in range(0, n):
        total += ((-1)**i)/((2*i) + 1)
    print(4*total)
    print(math.pi)




