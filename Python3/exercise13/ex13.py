#commandline parameters finally
from sys import argv

name, first, second, third = argv


print("Script name: ", name)
print("Param1: ", first)
print("Param2: ", second)
print("Param3: ", third)

#number of parameters
print("Parameter count: ", len(argv))

something = input("Type! ")
print("Got: ", something)
