from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take?")

    choice = input("> ")
    #checks to see if user entered a number
    if choice.isdigit():
        how_much = int(choice)
    else:
        dead("Man, learn how to type a number.")

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")


def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        choice = input("> ")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else: print("I got no idea what that means")


def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else: cthulhu_room()

def dance_room():
    print("You enter a dark room and hear a feint musical beat in the background.")
    print("Do you dance to the beat or act stiff?")

    choice = input("> ")

    if "dance" in choice:
        print("Dancing like Michael Jackson is the ultimate escape! You win!")
        exit()
    elif "stiff" in choice:
        dead("You are the death of the party. Die!")
    else:
        print("I don't understand what you just said")



def dead(why):
    print(why, "Good job!")
    exit(0)

def start():
    print("You are in a dark room.")
    print("There is a door to your right, a door to your left, and a door straight ahead.")
    print("Which one do you take?")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    elif choice == "ahead":
        dance_room()
    else:
        dead("You stumble around the room until you starve.")

start()
