print("Mary had a little lamb")
print("It's fleece was white as {}.".format('snow'))#will probably place snow into its place. 
print("And everywhere that Mary went")
print("." * 10) #expect to print 10 points after 'went'. No newline after all.
#welp I was wrong. didnt notice the implicit newlines before. Now I do.


#Cheeseburger
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "b"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

#fills  a variable called end with a space and also displays it
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
print(end7 + end8 + end9 + end10 + end11 + end12)
#removing it results in implicit newline, this way not. Interesting.
#end='' results in concatenated one-line string Cheeseburger. So thats how to keep it from newlining.
