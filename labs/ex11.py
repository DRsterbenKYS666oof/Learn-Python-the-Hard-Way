# end=' ' means to read the next line and put the next line on the same line where end=' ' is
print("How old are you?", end=' ')
# allows for user to put in info through the console
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()

#print(f...) is a way to format, which any curly brackets with a variable inside or whatever is inside
#will be printed in the console
print(f"So, you're {age} years old, {height} tall and {weight} lbs. heavy.")

#study drill 2 example
x = input('\nEnter your name:')
print('Hello, ' + x)
# Another example
beautiful_number = input("\ntell me a beautiful number: ")
print(beautiful_number)

#study drill 3
print("\nAre you a wiabu?", end=' ')
wiabu = input()
print("Are you a gamer?", end=' ')
gamer = input()

print(f"""Lets see your answers, {wiabu} and {gamer}.
Hhhhmmmmm...Interesting.""")