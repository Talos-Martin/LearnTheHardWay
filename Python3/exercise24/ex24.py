
print("Let's practive everything")
print('you\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs')


poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("-----------------")
print(poem)
print("-----------------")


five = 10 -  2 + 3 - 6
print(f"This better be five: {five}")

def secret_sauce(param):
    jelly_beans = param*500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates    #interesting. several return values


start_point=10000
beans,jars,crates = secret_sauce(start_point)

#Right. thats the way to not use f when you dont give one either
print("With a starting point of: {}".format(start_point))

print(f"We'd have {beans} beans, {jars} jars and {crates} crates")

start_point/=10 #divide by 10

print("Or we do it this way: ")
formula = secret_sauce(start_point)

#apply a list to a format string
print("We'd have {} beans, {} jars and {} crates".format(*formula))


