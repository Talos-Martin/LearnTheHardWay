ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("That wasn't 10. Let's fix that")

stuff = ten_things.split(' ')

more_stuff = ["Day", "Night", "Song" "Frisbee", "Corn", "Banana", "Girl", "Boy"]

#while(len(stuff)!=10):
for x in more_stuff:                    #exercise - for loop
        next_one = more_stuff.pop()
        print("Adding: ", next_one)
        stuff.append(next_one)
        print(f"There are {len(stuff)} items now")
        if len(stuff) >= 10:
                break

print("Have a look: ", stuff)

print("Let's do something with stuff")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print('*'.join(stuff))      #modified to better understand the previously 'empty' join
print("#".join(stuff[3:5]))

        
