## Boolean Algebra and Loops ##

## Boolean Algebra
# The Or operator returns true if one of the two values is true. In general, it starts grouping from the left by 2 then evaluates, then proceeds.
# True or False = True
# True or True = True
# False or True = True
# False or False = True

a = False
a or (1 == 1)

# The And operator returns true if both are true, else false. Groups the same way as or.
# True and False = False # is commutative
# False and False = False
# True and True = True

a = True
a and True

# The Not operator simply flips but can also be used to check things
# not True = False
# not False = True

# Ex1: If to implement: "For dessert, I'll have pie or ice cream"
ice = True
pie = False

if ((ice == True) and (pie == False)) or ((ice == False) and (pie == True)):
    print("I didnt lie about dessert")

if ice != pie: #both are not true or false
    print("I didnt lie about dessert")

if (ice and not pie) or (not ice and pie):
    #either ice and not pie, or not ice and pie
    print("I didnt lie about dessert")

# Ex2: growth mindset
lazy = False
smart = True
growmind = True

if not lazy and smart and growmind:
    print("Engsci")

elif lazy and smart and growmind:
    print("Physics")

elif not lazy and smart and not growmind:
    print("Econ")
elif lazy and not smart and not growmind:
    print("Ryerson")

# Ex3: Function returns with bools
def f():
    print("hello")
    return 1 + 2

print(f())



