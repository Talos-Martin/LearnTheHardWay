from sys import argv
import random




#########################################################################################################


def room_sphinx(name):
    number = random.randrange(1,51)
    print(f"\nI am the Sphinx, and you {name} will have to guess the correct number between 1 and 50")
    print("What is your first pick?")

    guess=0
    counter=0
    while(guess != number):
        counter+=1

        try:
            guess = int(input("> "))
        except ValueError:
            print("That was not an integer!")
            exit(-1)
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        elif(guess == number):
            print("Got it!")
        else:
            print("Integers only!")

    print(f"That took you {counter} tries")
    print("You may now proceed. Godspeed on your journey.")

    room_chambers(name)


#########################################################################################################

#not in use

def room_archive():
    #store something to a file and read it back
    file = open("secret.txt",'r+')
    password = file.readline()
    file.close
    if not password:
        print("Please set a password")
        password = input(" >")
        file = open("secret.txt", "w+")
        file.write(password)
        file.close()
        print("Thanks. You can leave now.")
        return 0
    else:
        print("What's the password?")
        compare = input("password: ")
        if compare == password:
            print("That's right!")
            print("Now leave me")
        else:
            print("Incorrect! Be gone!")
            return -1
#    print(f"Password is: {password}")

#########################################################################################################

def room_pathways(name):

    counter=0
    print("\nThere are three doors in this room, and a guard")                ##why are my newlines not displayed?
    print("Guard: \"Stop where you are or be slain without mercy!\"")
    print("Guard: \"What is your intention? Do you want to cross into one of the adjacent rooms?\"")

    while True:
        choice = input("> ")
        if choice == "yes":
            print("Guard: \"You could have said that right away! Bloody adventurers...\"")
            break
        elif choice == "no":
            print("Guard: \"What do you think this is? A waiting hall? Bloody adventurers...\"")
            print("Guard: \"Once again: Do you want to cross into one of the adjacent rooms?\"")
        else:
            print("Guard: \"What?? Is it 'yes' or 'no'!?\"")


    print("\nGuard: \"See!? That wasn't so hard\"")
    print("Guard: \"So, is it 'left', 'right' or 'center'?\"")

    while(True):
        choice = input("> ")
        if choice == "left":
            print("Guard: \"Left it is! Now begone. I have some guarding to do.\"")
            break
        elif choice == "right":
            print("Guard: \"That door is off limits since it leads to my private chambers.\"")
            print("Guard: \"Chose again.\"")
        elif choice == "center":
            print("Guard: \"Did you say 'left'? I'm pretty sure I heard you say left.\"")
            print("Guard: \"What was it you said?\"")
        else:
            print("Guard: \"Is said 'left', 'right' or 'center'!?\"")

    room_sphinx(name)



#########################################################################################################


def room_entrance(name):    #we'll start here
    print("Welcome to the maze, stranger")
    print(f"Here's your name tag. It reads {name}.")
    print("Never forget that. Forgetting is dangerous!")
    print("Now walk through that door on the right")

    whatever = input("> ")

    room_pathways(name)


#########################################################################################################


def room_chambers(name):    
    print("\nYou are in someones private chambers. ")
    print("By the looks and the smell you guess it belongs to a single older male inhabitant.")

    print("There's another door on the other side of the room. It slowly opens...")
    print("The old guard charges through, shriking like a banshee and leading with his sword")
    print("Guard: \"I told you my rooms are off limits! I will have your head for this privacy violation!!\"")

    print("You have to act quickly: Fight or flight?")

    while True:
        choice = input("> ")

        if choice == "fight":
            print("Let me say that again. I told you he has a sword. You are unarmed. Get it?? Fight or flight?")
        elif choice == "flight":
            print("A good choice! You manage to evade his first stroke, shove him out of the way and run past him out the door")
            print("You are pretty good at running away. Need that a lot, do you?")
            break
        elif "AAAAAAAAAAAAAAAAAAA" in choice:
            print("\nNice try. But this really isn't C")
            print("Your program doesn't die. You do.")
            exit(-1)
        else:
            print("I have no idea what that means. Now, is it 'fight' or 'flight'???")


    print("\nYou make it out of the maze alive. You are tremendously lucky. The last guy wasn't")
    print("He was made to guard the maze\n")

    exit(0)






#########################################################################################################

#So it begins....

script = argv
argc = len(argv)

if argc < 2:
    print(f"Usage: {script[0]} <Name>")
    exit(-1)
else:
    name = argv[1]

print("Welcome", name)

room_entrance(name)



