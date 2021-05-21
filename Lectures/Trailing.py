## Logic Check ##
a, b = 42, 43
a, b = b, a #swap

a, b = 42, 43 ##swap using a temp
temp = a
a = b
b = temp

# swap without second variable
a = 42
b = 43
a = a + b #42 + 43
b = a - b #42 + 43 - 43 = 42
a = a - b #42 + 43 - 42 = 43

## Loops example: Factorial ##
def fact(n):
    ''' does factorial of a function:
    factorial = 1 * 2 * 3... * (n-1) * (n)
    '''
    res = 1
    for i in range (1, n + 1):
        res *= i
    return res

def trailingzeroes(n):
    n = fact(n)
    zerocount = 0
    while n % 10 == 0:
        n //= 10
        zerocount+=1
    return zerocount

print("hello")
if __name__ == '__main__':
    print(trailingzeroes(10))




