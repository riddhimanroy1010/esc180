## Function definitions ##
def pirate_print(input_s): #input_s is the parameter
    print("Ahoy!", input_s + ". Yarr")

pirate_print("Hello") #"hello" is the argument of this function, Calling function later; must define function before using

def piratified_string(string): #returning things
    piratestring = "Ahoy! " + string + " Yarr!"
    return piratestring

print(piratified_string("hello"))

## Application 1 - Discriminant ##
def has_roots(a, b, c):
    #true if roots exist, else false
    disc = b**2 - 4*a*c
    if disc >= 0:
        return True
    else:
        return False

print(has_roots(1,1,2))

## Application 2 - inputing and returning nothing ##
def print_grade():
    print(grade)

def plunder_grade():
    global grade #global makes a variable global so other functions can access it
    grade = 0

grade = 100
plunder_grade()
print_grade()

## Application 3 - global and local variables ##
def f():
    return a + 10
    return b

def g():
    global a
    a = 5
    global b
    b = a + 10
    return b

print(f())
print(g())

## Application 4 - combining all of them ##
def adj_grade():
    global new_grade
    new_grade = grade + 1

def print_adj_grade():
    print(new_grade)

grade = 100
print_adj_grade()




