from sys import argv

script, filename = argv

def read_file(f):
    print(f.read())

def rewind_file(f):
    f.seek(0)

def print_line(number, f):
    print(number, f.readline(), end='') #why does just '' not work? Why does it have to be end=''? Why not without the variable? 


infile = open(filename)

print("Let's do this! Ex20! Whopee!")
read_file(infile)

print("Be kind, rewind!")
rewind_file(infile)

print("Line by line")
i=1;
print_line(i, infile)
#i++ #no workie?? surprise
i+=1
print_line(i, infile)
i+=1
print_line(i, infile)

