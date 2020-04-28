#comment
types_of_people = 10
#places string into string x
x = f"There are {types_of_people} types of people."

#playing with single and double quotes
binary = "binary"
do_not = "don't"
#placing those 2 strings into another string variable
y = f"Those who know {binary} and those who {do_not}"

##will display the 2 variables contents
print(x)
print(y)

#y in quotes. probably still just displays content normally
print(f"I said {x}")
print(f"I also said '{y}'")
#displays y as expected

hilarious = False
joke_evaluation = "Isn't that joke so funny!? {}"

#format false? Let's see what happens. And if I change to True
print(joke_evaluation.format(hilarious))
#That just printed False. I was expecting the format function to change the string somehow, based on the parameter(False). 
#instead it placed the variable contents in the place holder

#now string concatenation
w = "This is the left side of.."
e = "..a strong with a right side"
print(w+e)
