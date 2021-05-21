## Problem 1
def count_evens(L):
    '''
    Write a function with the signature def count_evens(L)
    that returns the number of even integers in the list L.
    Assume L only contains integers.
    '''
    num = 0
    for i in range(len(L)):
        if L[i] % 2 == 0:
            num += 1
    return num

## Problem 2
def list_to_str(lis):
    '''
    Without using str() with arguments that are lists
    (using it with arguments that are not lists is fine),
    write a function with the signature list_to_str(lis)
    which returns the string representation of the list lis.
    You may assume lis only contains integers.
    '''
    output = []
    for i in range(len(lis)):
        output.append(str(lis[i]))
    return output

## Problem 3
def lists_are_the_same(list1, list2):
    '''
    Without using the == operator to compare lists
    (you can still compare individual elements of the lists), '
    write a function lists_are_the_same(list1, list2)
    which returns True iff list1 and list2 contain
    the same elements in the same order.
    '''
    if len(list1) != len(list2):
        return False
    else:
        for i in range(len(list1)):
            if list1[i] != list2[i]:
                return False
    return True

## Problem 4
def simplify_fraction(n, m):
    '''
    Write a function with the signature simpify_fraction(n, m)
    which prints the simplified version of the fraction nm.
    For example, simplify_fraction(3,6) should print 1/2
    and simplify_fraction(8, 4) should print 2/1
    Hint: use a similar technique to the one we used when
    determining whether a number is prime. That is, try dividing
    both the numerator and the denominator by every possible divisor in turn.
    For example, if you are simplifying 16/12,
    you can try dividing both by 16, 15, 14, ...., 1.
    '''
    divisor = []
    for i in range(1, max(n, m)):
        if n % i == 0 and m % i == 0:
            divisor.append(i)
    gcd = max(divisor)

    print(str(int(n/gcd)) + "/" + str(int(m/gcd)))

## Problem 5
''' implementing the leibniz approximation for pi, from lab 3'''
import math
def leibniz_pi_approx(n):
    ''' n is degree of approximation.
    Formula: sum from 0 until n (-1)**n/(2n+1)'''
    total = 0
    for i in range(0, n):
        total += ((-1)**i)/((2*i) + 1)
    return(4*total)

def num_leibniz(n):
    iter = 0
    while int((leibniz_pi_approx(iter))*(10**(n-1))) != int(math.pi*(10**(n-1))):
        iter += 1
    return iter

## Problem 6
def euclid_simplify_fraction(a, b):
    '''implement the euclid algorithm for calculating the gcd. a, b in a set
    of natural numbers'''
    num1 = a
    num2 = b
    if (a or b) <= 0:
        return "Error, enter natural numbers"
    gcd = 1
    if max(a, b) % min(a, b) == 0:
        gcd = min(a, b)
    else:
        m = a % b
        while m != 0:
            m = a % b
            r = (a - m)/b
            a = b
            b = m
        gcd = max(a, b)

    print(str(int(num1/gcd)) + "/" + str(int(num2/gcd)))






