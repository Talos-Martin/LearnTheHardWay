people = 30
cars = 40
trucks = 15

if(cars > people):
    print("We should take the cars")
elif(cars < people):
    print("We should not take the cars")
else:
    print("We cannot decide")

if(trucks > cars):
    print("too many trucks")
elif(trucks < cars):
    print("Maybe trucks?")
else:
    print("Still undecided")

if(people > trucks):
    print("Alright, trucks it is")
else:
    print("lets stay home")

