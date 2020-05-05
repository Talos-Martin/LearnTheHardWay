import sys
script, input_encoding, error = sys.argv    #why not just argv?



#####################################################################################################################################################


#function main, reads a single line from file passed as parameter, calls printline to display input encoded and decoded
#then recursively calls itself with same parameters, file pointer is now at next line though
#stops when nothing more to read(end of file)

def main(language_file, encoding, errors):
    line = language_file.readline()
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)    #recursive call

#####################################################################################################################################################

def print_line(line, encoding, handle_errors):
    next_lang=line.strip()  #removes trailing \r\n? Need to look up. Yep, strips whitespace from end annd also beginning

    #encodes the line it read from the file as told via commandline, from UTF-8(see file open, where thats hardcoded)
    raw_bytes=next_lang.encode(encoding, errors=handle_errors) #weird errors use. why errors = errors?? / Changed variable name

    #decodes encoded line as told via commandline
    cooked_string=raw_bytes.decode(encoding, errors=handle_errors)

    print(raw_bytes, "<========>", cooked_string)

#####################################################################################################################################################


#entry point. script starts here
#languages=open("languages.txt", encoding="UTF-8") #opens file as UTF-8. Why is that necessary? Why not just open() without encoding specified? // UTF-16 doesn't work
languages=open("languages.txt") # seems to work just the same, without specifying the encoding?


#languages is the file handle for the just-opened file languages.txt
#input-encoding and error and from the commandline
main(languages, input_encoding, error)

#we have error set to 'strict' on the commandline:
# "Other possible values are 'ignore', 'replace', 'xmlcharrefreplace', 'backslashreplace' and any other name registered via codecs.register_error()."

#Other possible encoding values:
# https://docs.python.org/3/library/codecs.html#standard-encodings

#Exercise 3: rewrite using the b bytes,reversing the script. I don't understand what he wants me to do.
