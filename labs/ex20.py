# takes from sys (system), the import statement then puts the specific function, argv,
from sys import argv # to the console to be able to run properly

script, input_file = argv # <<<---command line arguments

def print_all(f): # cretaes the function 'print_all'
    print(f.read())
    
def rewind(f):
    f.seek(0)
    
def print_a_line(line_count, f):
    print(line_count, f.readline())
    
current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1 
print_a_line(current_line, current_file)

current_line = current_line + 1 
print_a_line(current_line, current_file)


__________________________________________________________________________________________
# to take from sys (system), the import statement then puts the specific function, argv,
from sys import argv # to the console to be able to run properly

script, input_file = argv # <<<---command line arguments

def print_all(f): # cretaes the function 'print_all' with f as a variable
    print(f.read()) # <<--will read the variable f, which will be a file, and print in the console
    
def rewind(f): # creates the function 'rewind' with f as a variable
    f.seek(0) # <<--?...
    
def print_a_line(line_count, f): # creates the function 'print_a_line' with variables
                                 # line_count and f
    print(line_count, f.readline()) # <<--?...
    
current_file = open(input_file) # variable that means, when used, to open the file 
                                # the variable is set to inside the parethesis
print("First let's print the whole file:\n") # <<--escape sequence that vertically tabs
                                             # one line down
print_all(current_file) # <<--uses the function print_all and the f variable becomes
                        # current_file
print("Now let's rewind, kind of like a tape.")

rewind(current_file) # <<--uses the function rewind and the f variable becomes 
                     # current_file
print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1 
print_a_line(current_line, current_file)

current_line = current_line + 1 
print_a_line(current_line, current_file)
