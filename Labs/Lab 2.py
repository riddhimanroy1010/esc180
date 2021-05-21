## Problem 1
if __name__ == "__main__":
    current_value = 0
    print("Welcome to the calculator program")
    print("Current value:", str(current_value))

## Problem 2
def display_current_value():
    print("Current Value:", current_value)

if __name__ == "__main__":
    current_value = 0
    print("Welcome to the calculator program")
    print("Current value:", str(current_value))
    display_current_value()

## Problem 3
def display_current_value():
    print("Current value:", current_value)

def add(to_add):
    global current_value
    current_value += to_add

def subtract(to_subtract):
    global current_value
    current_value -= to_subtract

if __name__ == "__main__":
    current_value = 0
    display_current_value()
    add(5)
    display_current_value()
    subtract(3)
    display_current_value()

## Problem 4
# I get an error as "undefined." I need to define a global variable inside the function I am working on, else that value cannot be reassigned.

## Problem 5
def display_current_value():
    print("Current value:", current_value)

def add(to_add):
    global current_value
    current_value += to_add

def subtract(to_subtract):
    global current_value
    current_value -= to_subtract

def multiply(to_mul):
    global current_value
    current_value = current_value*(to_mul)

def divide(to_div):
    if to_div != 0: #need this for /0 cases
        global current_value
        current_value = current_value/to_div
    else:
        print("Cannot Divide by 0")

if __name__ == "__main__":
    current_value = 0
    display_current_value()
    add(5) #5
    display_current_value()
    multiply(5) #25
    display_current_value()
    divide(0) #5
    display_current_value()
    divide(-1)
    display_current_value()

## Problem 6
def display_current_value():
    print("Current value:", current_value)

def add(to_add):
    global current_value
    current_value += to_add

def subtract(to_subtract):
    global current_value
    current_value -= to_subtract

def multiply(to_mul):
    global current_value
    current_value = current_value*(to_mul)

def divide(to_div):
    if to_div != 0: #need this for /0 cases
        global current_value
        current_value = current_value/to_div
    else:
        print("Cannot Divide by 0")

def sto():
    global sto
    sto = current_value
    print("Stored:", sto)

def rcl():
    print("Recalled:", sto)
    global current_value
    current_value = sto

if __name__ == "__main__":
    current_value = 0
    display_current_value()
    add(5) #5
    display_current_value()
    multiply(5) #25
    display_current_value()
    divide(0) #25
    display_current_value()
    sto() #25
    add(5) #30
    rcl() #25
    display_current_value() #25

## Problem 7
def display_current_value():
    print("Current value:", current_value)

def add(to_add):
    global current_value
    global lastval
    lastval = current_value
    current_value += to_add

def subtract(to_subtract):
    global current_value
    global lastval
    lastval = current_value
    current_value -= to_subtract

def multiply(to_mul):
    global current_value
    global lastval
    lastval = current_value
    current_value = current_value*(to_mul)

def divide(to_div):
    global current_value
    global lastval
    lastval = current_value
    if to_div != 0: #need this for /0 cases
        current_value = current_value/to_div
    else:
        print("Cannot Divide by 0")

def sto():
    global sto
    sto = current_value
    print("Stored:", sto)

def rcl():
    print("Recalled:", sto)
    global current_value
    current_value = sto

def undo():
    global current_value
    global lastval
    a = current_value
    current_value = lastval
    lastval = a

if __name__ == "__main__":
    current_value = 0
    display_current_value() # 0
    add(5) # 5
    subtract(2)
    display_current_value() # 3
    undo()
    display_current_value() # 5
    undo()
    display_current_value() # 3
    multiply(10)
    display_current_value() # 30
    undo()
    undo()
    display_current_value() # 30
    undo()
    undo()
    undo()
    display_current_value() # 3





