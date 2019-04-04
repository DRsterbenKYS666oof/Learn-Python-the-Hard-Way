#VVV takes from the system and the import searches for all the modules in Python
#VVV for the one you specified, in this case, argv
from sys import argv

script, said_filename = argv #<<<--- variables that are given on the command line
#VVV the f is the .format command that will fill in the variable and it's function in the
#VVV curly brackets
print(f"We're going to erase {said_filename}.")  # lines 7-9 will show exactly what
print("If you don't want that, hit CTRL-C (^C).")# they say in the console
print("If you do want that, hit RETURN.")

input("?") # allows for user interaction with the console

print("Opening the file...")
#VVV variable "target" is given the function to open the file in it's parameters
#VVV the 'w' also means the .write command, this allows for someone to write in the file and edit it
target = open(said_filename, 'w')

print("Truncating the file. Goodbye!")
# the variable is set to a file which is now going to be emptied by the command .truncate()
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")# allows for user interaction 3 times
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1) # .write command will allow for editing anything in the specified file.
target.write("\n")  # escape sequence, meaning go to the next line, being written down thorugh
target.write(line2) # the .write command
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close() # closes the file, kind of like saving it but as a function instead of a GUI
