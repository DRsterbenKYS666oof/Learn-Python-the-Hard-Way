# Set Varialbles down to line 8
name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
heightcm = height * 2.54
weight = 180 # lbs
weightkg = weight / 2.205
# Syntax to round up the number to a certain extent
round
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

# each string with an 'f' at the beginning makes it a format string
print(f"Let's talk about {name}.")
print(f"He's {heightcm} centimeters tall.")
print(f"He's about {weightkg} kilograms heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# This line is tricky, try to get it exactly right
# Another set variable with operations to equal an answer
total = age + heightcm + weightkg
print(f" If I add {age}, {heightcm} , and {weightkg} I get {total}.")