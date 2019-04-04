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
