from sys import argv

scriptname, filename = argv

#open file. not sure what modes are possible. need to look up
text = open(filename)

print(f"Here's the contents of {filename}:")
#print contents of file whose name is specified n parameter 'filename'
print(text.read())
text.close()


print("Tell me the filename again: ")
newfile=input("Filename: ")

file2 = open(newfile)
print("Content here: ")
print(file2.read())
file2.close()
