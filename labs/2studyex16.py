from sys import argv

script, tiger_duck = argv

open_sesame = open(tiger_duck)

print(f"Lets open up one of your files >> {tiger_duck}")

print("Now lets open it.")
print(open_sesame.read())