## Passing information to and from functions ##
## Example 1
def has_roots(a, b, c):
    global disc #making this a global variable so other parts of the function can use it
    disc = b**2 - 4*a*c
    return disc > 0

print(has_roots(2, 3, 4))
print(disc)

## Example 2
def adj_grade():
    global new_grade
    new_grade = grade + 1

def print_adj_grade():
    print(new_grade)

grade = 100
print_adj_grade()
## main function seperator
if __name__ == "__main__":
    #body
    print("hello") #use this to seperate main function from self defined functions

## Boolean variables ##
a = (1 != 2) #true
b = (1 > 200) #false

a and b #and returns true if both are true else false
a or b #or returns true if either one is true
