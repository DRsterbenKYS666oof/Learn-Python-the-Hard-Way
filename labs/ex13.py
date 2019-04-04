# Takes from the system and the import searches for all the
# modules in Python for the one you specified
from sys import argv
# read the WYSS section for how to run this
script, first, second, third, fourth = argv # <<<--command line argument variables

# The variables are printed from the command line arguments and fill in the spots in order
# of where they are typed
print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
#VVV My addition VVV
print("Your fourth variable is:", fourth)