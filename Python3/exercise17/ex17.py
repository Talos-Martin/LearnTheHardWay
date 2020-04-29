from sys import argv
from os.path import exists

script, from_file, to_file = argv

#print(f"Hello world")

print(f"Let's copy file {from_file}")

#infile = open(from_file, "r")
#inbuf = infile.read()
#unifying into a single line
inbuf = (open(from_file, "r")).read()

print(f"This file is {len(inbuf)} bytes long")

print(f"Does the output exist? {exists(to_file)}")
print("Hit enter when ready")

input()

outfile=open(to_file,'w')
outfile.write(inbuf)

print("Close the files")

#infile.close() #have to comment this out because with a single line open/read, theres no file handle assigned to a variable
outfile.close()




