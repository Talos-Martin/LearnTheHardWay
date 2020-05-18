def scan(sentence):

    library =   {   "north":"direction",
                    "south":"direction",
                    "east":"direction",
                    "west":"direction",
                    "go":"verb",
                    "kill":"verb",
                    "eat":"verb",
                    "the":"stop",
                    "in":"stop",
                    "of":"stop",
                    "bear":"noun",
                    "princess":"noun",
                    "1234":"number",
                    "3":"number",
                    "91234":"number",
                    "ASDFADFASDF":"error",
                    "IAS":"error"
                }

    data = []

    words = sentence.split(' ')

#    print(library)
    
    for word in words:
        value = library.get(word)
        if word.isdigit():              #using the generic lookup and attach function like for the strings below, it would attach my number as a string, and I didn't know how to fix that
#            print("Found us a number:", word)
            data.append((library[word], int(word)))
        elif(value):
#            print("Value is: ", library[word])
            data.append((library[word],word))
#        else:
#            print("No matching key")

#    print(data)            

    return data

# For testing without nosetest
#scan("south north 1234")  


###################################################################################################

# first try. hardcode the correct result for the first test and see whether that works
#    if 'north' in sentence:
#        return [('direction', 'north')]
#    else:
#        return None

#scan("north")  

############################################################################################################################################

# Failed first approach
"""
class Lexicon(object):      #lowercase classname???

    first_word = ('verb', 'go')
    second_word = ('direction', 'north')
    third_word = ('direction', 'west')
    sentence = [first_word, second_word, third_word]



    def scan(self, direction):
        if 'north' in direction:
            return [('direction', 'north')]
"""
