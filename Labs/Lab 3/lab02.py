## Learning goals
# * Write simple functions
# * Pass information to a function via parameters
# * Pass information to a function via global variables
# * Return information from functions via return values and global variables
# * Use global variables as "static" information

def display_current_value():
    '''Display the current value

    '''
    print('Current value:', current_value)

def save_value():
    '''Save the current value for furture use

    '''

    global prev_value
    prev_value = current_value

def add(to_add):
    '''Add to_add to the current value
    Arguments:
    to_add: an integer to add to the current value

    '''

    global current_value
    save_value()
    if current_value != "ERROR":
        current_value += to_add

def subtract(to_subtract):
    '''Subtract to_subtract from the current value

    '''

    global current_value
    save_value()
    if current_value != "ERROR":
        current_value -= to_subtract

def multiply(to_mult):
    '''Multiply the current value by to_mult

    '''

    global current_value
    save_value()
    if current_value != "ERROR":
        current_value *= to_mult

def divide(to_divide):
    '''Divide the current value by to_divide if to_divide != 0, set the current
    value to 'ERROR' otherwise

    '''

    global current_value
    save_value()
    if current_value != "ERROR":
        if to_divide == 0:
            current_value = 'ERROR'
        else:
            current_value /= to_divide

def store():
    '''Emulate the memory button by storing the current value for future use
    Note: cannot be undone with the undo() button
    '''
    global mem_value
    mem_value = current_value

def recall():
    '''Emulate the recall button by retriving a stored memory value

    '''
    global current_value
    current_value = mem_value

def undo():
    '''Make the current value have the value it had before the last operation

    '''
    global current_value, prev_value
    current_value, prev_value = prev_value, current_value



def initialize():
    global current_value, prev_value, mem_value
    current_value = 0
    prev_value = 0
    mem_value = 0

def get_current_value():
    return current_value


if __name__ == '__main__':
    ################################################################
    #Typical cases

    #Typical cases for add and subtract
    #(Should also test for divide and multiply)
    initialize()
    add(5)
    display_current_value() #expected output: 0+5=5


    current_value = 15
    subtract(7)

    display_current_value() #expected output: 15-7=8

    ########################################################################
    #Typical cases

    #Test for interactions between the different functions

    initialize()
    add(5)
    subtract(10)
    multiply(2)
    display_current_value() #expected output: (5-10)*2 = -10
                            #handles negative numbers?
                            #handles interactions between add(), subtract()...




    #Other things to test for:
    #undo() twice
    #use both undo() and recall()
    #recall() and then undo()
    #undo(), recall(), add(), ... all together (maybe do a couple tests like that)

    ##########################################################################


    #try adding negative number:
    initialize()
    add(-5) #expected output: 0-5=-5


    #try an "irrational" number:
    import math
    current_value = 42
    divide(math.pi)
    display_current_value() #expected value: approx. 13.36901521971921


    ##########################################################################
    #Boundary case:
    #Something that involves zero
    initialize()
    add(5)
    subtract(5)
    display_current_value() # expected: 5-5 = 0

    #try adding zero:
    current_value = 5
    add(0) #expected output: 5+0=0

    ###########################################################################
    #Error cases:
    #try dividing by 0

    current_value = 10
    divide(0)
    display_current_value() #expected output: ERROR



    #produce an error, then try adding 10
    current_value = 10
    divide(0)
    add(5) #expected output: you should decide


    ###########################################################################
    #Special cases where you might expect problems

    #Divide by a very large number (so as to get 0), then multiply by the same
    #number


    #add a very large number to another large number, see if there's a limit
    #to the number of digits

    #divide 0 by 0

    #can you undo an "ERROR"?
    #can you store "ERROR"
    #try adding 5 to "ERROR"