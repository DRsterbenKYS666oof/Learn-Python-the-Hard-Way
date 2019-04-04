# first of all, def means "define"; it creates functions.
# before the parameters is where the name of the function created is.
# (*args) is a lot like an argv parameter except it's for functions, also it has to be in parenthesis to work
def print_two(*args): # <<<--- the colon will indent the following lines to attach the lines to the name, print_two; "mini scripts".                                                          # this one is like your scripts with argv
    arg1, arg2 = args # <<--unpacks arguments, makes a tuple into separate variables
    print(f"arg1: {arg1}, arg2: {arg2}")  0# this is an f string, this allows for variables to be substituted
    
# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2): # <<<---instead of unpacking arguments, the variables are separate in the parenthesis
    print(f"arg1: {arg1}, arg2: {arg2}")
    
# this just takes one argument
def print_one(arg1): 
    print(f"arg1: {arg1}")
    
# this one takes no arguments
def print_none(): 
    print("I got nothin'.")
    
print_two("Gabriel","Nadow") # stating what arg1 and arg2 means for each def function
print_two_again("Cassandra","Gollaz")
print_one("First!")
print_none()
