#function accepts two parameters and prints them
#input is an array
def print_two(*args):
    arg1, arg2 = args
    print(f"args are: {arg1} and {arg2}")

#input is two values(not an array)
def two_again(arg1, arg2):
    print(f"args are: {arg1}, {arg2}")

def one_arg(argument):
    print(f"Just one arg: {argument}")

def no_arg():
    print("Hello there")

#calling our 4 functions
print_two("John", "Doe")
two_again("Jane", "Doe")
one_arg("No_Doe")
no_arg()




