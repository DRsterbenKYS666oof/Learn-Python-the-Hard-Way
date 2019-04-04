#VVV takes from the system and the import searches for all the modules in Python
#VVV for the one you specified, in this case, argv
from sys import argv
#VVV the first line in the bash console is called the command line and these
#VVV are command line argument variables
script, filename = argv

txt = open(filename)#<<<-- Variable txt has a meaning of open(filename)

print(f"Here's your file {filename}:")#<<<-- format string: replaces a variable
print(txt.read())                     #      when placed inside the curly brackets
#^^^ Fills in the variable txt and the .read is a command to read a file
#^^^ which is just what the txt variable so happens to have, a file.

print("Type the filename again:")
file_again = input("> ")#<<<-- this variable has a meaning with input, python will
                        # read input and want an answer fro the user. Whatever
                        # is in the paranthesis next to input will show up firt in the console

txt_again = open(file_again)#<<<-- variable text_again means open(file_agian)

print(txt_again.read())
#^^^ fills in the variable and the .read is a command to read a file, in this case
#^^^ it wants to print using the input from the other variable to read that variable