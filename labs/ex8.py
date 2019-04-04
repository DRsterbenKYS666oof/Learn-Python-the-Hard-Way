# formatter is the set variable for ""
# the {} are right now only set to be a temporary PLACEHOLDER
formatter = "{} {} {} {}"

# using .format to fill in the curly brackets for the variable, formatter
print(formatter.format(1,2,3,4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Stamp on",
    "The ground, Jump",
    "Jump, Jump, Jump,",
    "Moving all around"
))