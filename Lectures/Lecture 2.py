import math

a = 1
b = 10
c = 2

disc = b**2 - 4*a*c
if disc > 0:
    r1 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
    r2 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)
    print("Two roots: " + r1 + ", " + r2)
elif disc == 0:
    print ("One repeated root: " + r1)
else:
    print("No real roots")