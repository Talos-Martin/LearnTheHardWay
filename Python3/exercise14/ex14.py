from sys import argv

script, name = argv

prompt = '> '

print(f"Hello {name}, I am {script}")
print("Questions follow")
print(f"Do you like coding {name}?")
answer=input(prompt)

print("Here comes the second question?")
second=input(prompt)

print(f"And the third question from {script}?")
third=input(prompt)

print(f"""Well well well,
if this isn't {name},
talking to {script},
on his {third}""")


