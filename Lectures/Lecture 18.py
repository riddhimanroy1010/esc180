def n_as_plus_b(s):
    '''Return the maximum number of a's followed by a 'b' in the string'''
    for length in range(len(s), -1, -1):
        if "a" * length + "b" in s:
            return length

def n_as_plus_b2(s):
    pass

alpha = "dnjkfbf"

def password_gen(alpha):
    for c1 in alpha:
        for c2 in alpha:
            for c3 in alpha:
                print(c1 + c2 + c3)
##Exec
code = '''def f():
    return 5
    '''
exec(code)

##substitution
s = "I got {} on the calc midterm".format(12)

##Write a function with a nested loop with N levels that prints all the
##passwords of length N
def password_gen_2(alpha, N):
    code = ""
    for i in range(N):
        code += "for c{} in alpha:\n".format(i)
        code += "  " * (i + 1)
    code += "print("
    for i in range(N - 1):
        code += "c{}".format(i) + " + "
    code += "c{}".format(N - 1)
    code += ")"
    exec(code)


if __name__ == "__main__":
    n_as_plus_b("aab")

