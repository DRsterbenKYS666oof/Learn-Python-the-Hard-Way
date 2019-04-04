types_of_people = 10
# lines 3 and 7 format (the beginning f) inside the variable to replace any
# variable used in the curly brackets when that variable is used
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)
# lines 11 and 12 use the format (the beginning f) to substitute a variable
# that's inside the curly brackets
print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
# curly brackets at the end represents a place holder when it's empty
joke_evaluation = "Isn't that joke so funny?! {}"
# .format is to to fill in a place holder
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."
# adding combines 2 numbers, so here it's going to combine the two variables and
# their meaning
print(w + e)