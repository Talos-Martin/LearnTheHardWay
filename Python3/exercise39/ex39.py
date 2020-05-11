states = {'Oregon':'OR', 'Florida':'FL', 'California':'CA', 'New York':'NY', 'Michigan':'MI'}
states['Bavaria'] = 'BY'    #exercise

cities = {'CA':'San Francisco', 'MI':'Detroit', 'FL':'Jacksonville'}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'
cities['BY'] = 'Munich'     #exercise

print("-" * 10)

print("NY state has ", cities['NY'])
print("Oregon state has ", cities['OR'])

print("#" * 10)

print("Michigans abbreviation is", states['Michigan'])
print("Floridas abbreviation is ", states['Florida'])



print("X" * 30)

print("Michigan has ", cities[states['Michigan']])
print("Florida has ", cities[states['Florida']])

print("*" * 50)

for state, abbrev in list(states.items()):
    print(f"{state} is shortened to {abbrev}")

print("3" * 30)

for abbrev, city in list(cities.items()):
    print(f"{abbrev} has {city}")

print("XXX" * 10)

for state, abbrev in list(states.items()):
    print(f"State {state} is {abbrev} ")
    print(f"and has city {cities[abbrev]}")

print("-" * 10)

state = states.get('Texas')

if not state:
    print("Welp, Texas is a myth")

#print(f"Jacksonville is in {cities['Jacksonville']}")   #reverse lookup - no workie - so it's a strict key/value pair it seems

city = cities.get('TX', 'Does not exist')   #Confusing. I had to look up that function. It seems 'Does not exist' as a value for the key 'TX' was added. 

for abbrev, cityname in list(cities.items()):  #making sure TX has not been inserted into the list
    print(f"City is {cityname}")

print(f"The city for the state TX is {city}")   #'city' got the default return value of "Does noit exist" when get() failed to find key TX in cities

print("#" * 30)

print(cities.items())
print(cities.keys())

print("-_-" * 30)

states.setdefault('WRL')
for state, abbrev in list(states.items()):
    print(f"{state} is shortened to {abbrev}")


states.setdefault('WRL2','Now')
for state, abbrev in list(states.items()):
    print(f"{state} is shortened to {abbrev}")


print("'" * 50)

more_states = {'Oregon':'ORRO', 'Texas':'TX'}
states.update(more_states)

for state, abbrev in list(states.items()):
    print(f"{state} is shortened to {abbrev}")




