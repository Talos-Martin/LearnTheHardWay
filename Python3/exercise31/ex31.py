print("You enter a dark room. There are two doors. Will you go through door #1 or door #2?")
door = input("> ")

if door == "1":
    print("There's a giant bear here eating cheesecake.")
    print("What do you do?")
    print("1) Take the cake\n2) Scream at the bear")
    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off. Great job!")
    elif bear == "2":
        print("The bear eats your legs off. Great job!")
    else:
        print(f"Thruth be told, {bear} was probably better")
        print("The bear runs off")

elif door=="2":
    print("You stare into the endless abyss at Ctulhu's retina")
    print("1) Blueberries")
    print("2) Yellow jacket clothespins")
    print("3) Understanding revolvers yelling melodies")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello")
        print("Good job!")
    elif insanity == "3":
        print("The exercise is well done. Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck!")
        print("Good job!")
else:
    print("You stumble around and fall into a knife and die. Good job!")







