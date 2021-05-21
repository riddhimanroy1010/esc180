############# Printing multiple values ############
print("Hello engsci")

print("Hello" + " " + "Engsci")

subj = "Indy"

print("Hello, " + subj)

prog_rating = 7.9
print(subj, prog_rating)

prog_rating = "7.9"
print(subj + ": " + prog_rating)

############## printing #############
"A"
#or
"'A'"
#or

a = '''abc
def
ghi'''

print(a)

############ data types ##################
a = "string" #string
b = 2 #integer
c = 4.2e800000000000000#float, limited in magnitude (powers of 10), but can store fractions

#max and min values for floats
import sys
sys.float_info.max
sys.float_info.min

################# casting ##################

#string to float
prog_rating = 7.9
subj = "Indy"
print(subj , str(prog_rating))

#float to string
rating = "1"
a = float(rating)*10

#float to integer
a = int(5.2)

#rounding is different
round(5.5)

#nested casting
int(float(5.2))

#specified rounding
round(5.21287182712,1) #1sd
round(5.21287182712, 3) #3sd

############## Quadratic Equation solver application #############
import math

a = 1
b = 10
c = 2

disc = b**2 - 4*a*c
if disc > 0:
    r1 = (-b + math.sqrt(disc))/(2*a)
    r2 = (-b - math.sqrt(disc))/(2*a)
    print("Two roots: " + str(r1) + ", " + str(r2))
elif disc == 0:
    print ("One repeated root: " + str(r1))
else:
    print("No real roots")


