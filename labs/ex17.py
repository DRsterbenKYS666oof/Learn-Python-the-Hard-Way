# takes from 'sys' (system) and whats taken is 'argv' through the import statement
from sys import argv
# takes from 'os.path' (something idk) and what's taken is 'exists' through the import statement
from os.path import exists

script, from_file, to_file = argv # <<<---command line arguments

print(f"Copying from {from_file} to {to_file}")# <<<---f is a different way of .format() or formatter.format()
                                               #       which can substitute variables, use functions, etc.
# we could do these two on one line, how?
in_file = open(from_file) # <<<---variable 'in_file' is set to open a file in its parameters
indata = in_file.read() # <<<---variable 'indata' is set to have variable 'in_file' be read with
                              # the command .read()
print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input() # <<<---allows for user interaction

out_file = open(to_file, 'w')# <<<---variable 'out_file' is set to open a file in its parameters
                                   # and to be put in write mode with 'w'
out_file.write(indata)# <<<---'out_file' will have anything written to its meaning with the 
                            # .write() command; the parameters can be used to have whatever is inside
                            # to be written to 'out_file'
print("Alright, all done.")

out_file.close() # .close() will close a file and when it closes it, it saves the file as well
in_file.close()
