def halt(function_text, function_input):
    '''
    Return true if the function halts (there is no infinite loop)
    '''
    pass

def confused(f):
    if halt(f, f):
        while True:
            pass
    else:
        return False

# confused(confused)
# suppose halt(confused, confused) is True. So confused(confused) halts. Therefore confused(confused) doesn't halt
# suppose halt(confused, confused) is False. So confused(confused) doesn't halt. But if halt(confused, confused) doesn't halt,
# then confused(confused) does halt
#
# Therefore, it is impossible to write this kind of function
# 