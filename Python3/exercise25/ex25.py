def break_words(stuff):
    """This function breaks up words"""
    return stuff.split(' ')

def sort_words(stuff):
    """sort_wordds comment"""
    """what about two comments?"""      #not displayed in help
    return sorted(stuff)

def print_first_word(words):
    """print first word comment"""
    word=words.pop(0)
    """And later in the function?"""    #not displayed in help
    return  word

def print_last_word(words):
#    """print last word now"""
    word = words.pop(-1)
    """laters"""                        #not displayed in help
    return word

def sort_sentence(sentence):
    """sorting sentence"""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """well first and last no order"""
    words=break_words(sentence)
    print_first_word(words)
    print_last_word(words)


def print_first_and_last_sorted(sentence):
    """first and last ordered"""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


