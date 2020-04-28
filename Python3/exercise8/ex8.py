#4 placeholders for content
formater = "{} {} {} {}"

#should print the 4 numbers with spaces in between
print(formater.format(1,2,3,4))

#should print the 4 words with spaces in between
print(formater.format("one", "two", "three", "four"))

#should print the 4 words, even though they are not strings, but truth statements
print(formater.format(True, False, False, True))

#will print the string 4 times, so 16 braces. nothing to fill into specified after all
print(formater.format(formater, formater, formater, formater))

#will print my strings with spaces. implicit newlines?
print(formater.format(
                        "We",
                        "pwn",
                        "the",
                        "world"
                    ))
#ok no newlines, just spaces
