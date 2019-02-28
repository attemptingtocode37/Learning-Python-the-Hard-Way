def heaven():
    print("Jesus christ welcomes you to heaven. Have you committed sin on your travels?")

    answer = input("> Yes or no? ").lower()
    if "yes" in answer:
        print("Honesty takes courage. Go to the clinic.")
        exit(0)
    elif "no" in answer:
        print("Lying is a sin. Now you are double sinning")
        hell("Close but no cigar.")
    else:
        print("Read the prompt you fool.")


def asia():
    print("Welcome to traveller central. You have arrived at the hostel.")
    print("Do you make friends, go to bed, or get steaming?")
    oohfriends = False

    while True:
        answer = input("> ").lower()

        if "bed" in answer:
            print("That's not the point, go to hell!")
            hell("Fool.")
        elif "friends" in answer and not oohfriends:
            print("You've made a friend while sober. Well done you aren't a freak.")
            print("You can have a drink with them now and become besties in a few hours.")
            oohfriends = True
        elif "steaming" in answer and oohfriends:
            heaven()
        elif "steaming" in answer and not oohfriends:
            print("Now now, you don't want to make a fool of yourself!")
        else:
            print("Come again?")


def work():
    print("Welcome to the rat race.")
    print("Do you want to chase the highest position in the first career that you try?")

    choice = input("> ").lower()

    if "yes" in choice:
        hell("You will be the master of air flow.")
    if "no" in choice:
        print("Great decision, reevaluate your options.")
        start()

def further_edn():
    print("You blasted fool. You will be penny pinching for eternity you peasant!")
    hell("Have a nice trip to hell.")

def hell(why):
    print(why, "Good riddance!")
    exit(0)

def start():
    print("You have just graduated with a top degree!")
    print("You are in £50,000 of debt")
    print("You have 3 options")
    print("Do you travel, work, or go into further education?")

    choice = input("> ").lower()

    if "travel" in choice:
        asia()
    elif "work" in choice:
        work()
    elif "education" in choice:
        further_edn()
    else:
        dead("You go off into the abyss")

start()
