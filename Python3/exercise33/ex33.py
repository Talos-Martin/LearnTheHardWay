numbers = []

def adder(max, diff):
    i=0   
    while i < max:
        print(f"At the top i is {i}")
        numbers.append(i)

        i+=diff
        print("Numbers now ", numbers)

        print(f"At the bottom i is {i}")
    
def adderer(max):
    i=0   
    for i in range(0,max):
        print(f"At the top i is {i}")
        numbers.append(i)

        i+=1
        print("Numbers now ", numbers)

        print(f"At the bottom i is {i}")
    


#adder(8,2)
adderer(4)

print("The numbers: ")
for num in numbers:
    print(num)

