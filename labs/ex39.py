# create a mapping of state to abbreviation 
states = { 
    'Oregon': 'OR', 
    'Florida': 'FL', 
    'Californa': 'CA', 
    'New York': 'NY', 
    'Michigan': 'MI', 
} 

# create a basic set of states and some cities in them 
cities = { 
    'CA': 'San Francisco', 
    'MI': 'Detroit', 
    'FL': 'Jacksonville' 
} 

# add some more cities 
cities['NY'] = 'New York' 
cities['OR'] = 'Portland' 

# print out some cities 
print('-' * 35) 
print("NY State has: ", cities['NY']) 
print("OR State has: ", cities['OR']) 

# print some states 
print('-' * 35) 
print("Michigan's abbreviation is: ", states['Michigan']) 
print("Florida's abbreviation is: ", states['Florida']) 

# do it by using the state then cities dict 
print('-' * 35) 
print("Michigan has: ", cities[states['Michigan']]) 
print("Florida has: ", cities[states['Florida']]) 

# print every state abbreviation 
print('-' * 35) 
for state, abbrev in list(states.items()): 
    print(f"{state} is abbreviated {abbrev}") 

# print every city in state 
print('-' * 35) 
for abbrev, city in list(cities.items()): 
    print(f"{abbrev} has the city {city}") 

# now do both at the same time 
print('-' * 35) 
for state, abbrev in list(states.items()): 
    print(f"{state} state is abbreviated {abbrev}") 
    print(f"and has city {cities[abbrev]}") 

print('-' * 35) 
# safely get an abbreviation by state that might not be there 
state = states.get('Texas') 

if not state: 
    print("Sorry, no Texas.") 

# get a city with a default value 
city = cities.get('TX', 'Does Not Exist') 
print(f"The city for the state of 'TX' is: {city}") 
