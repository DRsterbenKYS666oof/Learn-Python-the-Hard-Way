print("Mary had a little lamb.")
#a format is made after ending the quotes to fill in the curly brackets(my comment)
print("It's fleece was as white as {}.".format("snow"))
print("And everywhere that Mary went.")
#Multiplies the period 10 times(my comment)
print("." * 10) # what'd that do?

# lines 6-17 are setting up variables to equal something
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end. try removing it to see what happens
# after the comma, a variable is created and used at the same time (my comment).
# both of the next two lines add the letters after one another, "combining" the letters together.(my comment)
# If comma is removed, a syntax error appearsmy(my comment)
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
print(end7 + end8 + end9 + end10 + end11 + end12)