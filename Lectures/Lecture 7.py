## Useful for Project 1 ##
7/2 # 3.5
7 // 2 # integer division, 3
7 % 2 # modulo, remainder of divison
7 == 2 * (7 // 2) + (7 % 2)

## For loops ##
for i in range(5):
    print(i)
    print(i+2)
    print("===================")

for i in range(5):
    if i + 1 == 1:
        print("For the" + " " + str(i+1) + ("st time, I like physics"))
    elif i + 1 == 2:
        print("For the" + " " + str(i+1) + ("nd time, I like physics"))
    elif i + 1 == 3:
        print("For the" + " " + str(i+1) + ("rd time, I like physics"))
    else:
        print("For the" + " " + str(i+1) + ("th time, I like physics"))

## While Loops ##
def log10(n):
    res = 1
    i = 0
    while res < n:
        res = res * 10
        i+=1
    return i

print(log10(100))

def isprime(n):
    ''' return true iff prime; n > 0 '''
    if n <= 1:
        return False
    elif n == 2:
        return False
    else:
        for i in range(n - 2):
            if n % (i + 2) == 0:
                return False

    return True
