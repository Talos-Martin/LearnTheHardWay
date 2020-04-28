#first input from commandline exercise

print("what's the weight of a swallow?")    #removing end statement makes input read from new line, not same line
weight=input();
print("European or African? How old??", end=' '); #end='' removes space. space between sentence and input can also be achieved by placing extra space after question mark, before closing quote
age=input();
print("Does the size of the bird matter??", end=' ');
height=input();

print(f"""So here we have a swallow with a weight of {weight},
        an age of {age},
        and a height of {height}""")

#input list(2 variables here)
#input function called with descriptive string
#split with no argument, to separate by space
age, eight = input("Age and weight please. Separate by space. No Lies!").split()
print("Age is", age, "and weight is", weight);
