from sys import argv

script, name = argv

print(f"We are going to truncate {name}.")
print("Make sure you really want that!")

print("File opening")
handle = open(name, 'r')

print("File contains: ")
print(handle.read())

#Close the file. Otherwise I can't truncate
handle.close()


print("Erase File?? (Ctrl-C to break)")

decision = input("> ")

print("File opening")
handle = open(name, 'w')

print("Truncating!")
handle.truncate()

print("Now gimme 3 lines: ")

line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print("Writing these into the file")
#handle.write(line1)
#handle.write("\n")
#handle.write(line2)
#handle.write("\n")
#handle.write(line3)
#handle.write("\n")

#Drill
#handle.write(line1, "\n", line2, "\n", line3, "\n") #nope
buf = line1 + "\n" + line2 + "\n" + line3 + "\n"  
handle.write(buf)

print("Time to close the file")
handle.close()


