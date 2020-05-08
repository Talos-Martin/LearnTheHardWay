from sys import exit

def gold_room():  #awesome remixes. especially "mother protect - nikki and the dove"
    print("This room is full of gold. How much do we take?")    #All of it obviously. What kinda stupid question is this??

    choice = input("> ")
    if "0" in choice or "1" in choice:      #1 is ok. So is 10. 49 is not. 41 is though, but not 51
        how_much = int(choice)
    else:
        dead("Learn to type a number")

    if how_much < 50:
        print("Nice. You're not greedy. You win!")  #fool!
        exit(0)
    else:
        dead("You greedy bastard")

def bear_room():
    print("There is a bear here")   #same bear that ate my face and legs??
    print("The bear has a bunch of honey")
    print("The slightly overweight bear is in front of a door")
    print("How are we going to move the bear?")
    bear_moved = False

    while True:         #dangerous. Might loop forever if not careful
        choice = input("> ")
#        print("Choice was: #", choice, "#")
        if choice == "take honey":
            dead("Wtf man are you stupid? Don't you remember what happened to your face and legs???")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door. You can pass through now")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear is pissed and tries to chew your legs off. Again. Wanker!")
        elif choice == "open door" and bear_moved:
            gold_room()
        elif choice == "open door" and not bear_moved:
            print("The bear and you become best buddies. He shares his honey with you. It's great stuff. Then he tells you about the gold room, but you don't believe a word, and you start taunting him")
        else:
            print("I have no idea what that's supposed to mean")

def cthulhu_room():
    print("Here you see the great evil Chtulhu. (Lucky you, he's no bear)")
    print("He stares at you and you go insane")
    print("Flee for your life or eat your head?")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("That was tasty!")
    else:
        cthulhu_room()

def dead(why):
    print(why, "Good job!")
    exit(0)


def start():
    print("You are in a dark room. There are two doors, left and right. Chose wisely")

    choice = input("> ")
    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        print("You stumble around until you starve. Good job once again")

start()
