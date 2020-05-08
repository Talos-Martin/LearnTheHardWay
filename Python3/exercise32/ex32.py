the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'apricots', 'pears']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for number in the_count:
    print(f"This is loop number {number}")

for fruit in fruits:
        print(f"This is fruit {fruit}")

for i in change:
    print(f"That's {i}")

elements = []

#for i in range(0, 6):
#print(f"Adding number {i}")
#    elements.append(i)

#elements.append(0,1,2,3,4,5)   #nope
elements.append(0)
elements.append("1")
elements.append(2)
elements.append("3")
elements.append(4)
elements.append("5")



for i in elements:
    print(f"Elements1: {i}")

removed = elements.pop()
elements.extend(fruits)
for i in elements:
    print(f"Elements2: {i}")

elements.pop(-1)
for i in elements:
    print(f"Elements3: {i}")




