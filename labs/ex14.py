#VVV takes from the system and the import searches for all the
#VVV modules in Python for the one you specified
from sys import argv

script, user_name = argv # <<<-- command line arguement variables
# variable is set to a print > and a space making '> '
prompt = '> '

# format strings on lines 10, 12, and 17 replaces with a variable already given the meaning of
print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)#<<< lines like this have a variable that print the variable, prompt,
                     # and then want an answer from the user using input
print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)
#VVV all inputs will become the meaning of the variables that will be put instead of the
#VVV curly brackets using format
print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")