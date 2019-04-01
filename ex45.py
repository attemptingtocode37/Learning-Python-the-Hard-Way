# My Own Game
# Engine to run the Game
# Map to navigate
# Use import to import a module
# One class per room
# Return next room in each room

# Rambo Story
# Rambo is called out to a mission in London
# He has to battle roadmen > yuppies > albanian gangsters
# Roadmen - Croydon
# Yuppies - Clapham
# Albanian - Hounslow
# When in Hounslow, he has to call on Chabuddy G for help. Chabuddy kills the Albanian boss
# Rambo and Chabuddy head off to Hakkasan for a romantic celebratory meal

from sys import exit
from textwrap import dedent
from rndm import rndm_no_gen
from random import randint


class Scene(object):

    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)


class Engine(object):

# A scene_map object is instantiated when class Engine is called
    def __init__(self, scene_map):
        self.scene_map = scene_map

# Defines a method play
    def play(self):
# Creates 2 attributes. current_scene returns the value of the start_scene
        current_scene = self.scene_map.opening_scene()
# last_scene returns the Class when 'finished' is the argument
        last_scene = self.scene_map.next_scene('finished')

# while the current_scene does not equal the last_scene
        while current_scene != last_scene:
# Returns the value from the current scene and sets it to next_scene_name
            next_scene_name = current_scene.enter()
# Return the class from the return value in next_scene_name
            current_scene = self.scene_map.next_scene(next_scene_name)
# Calls enter on that class. return value in class links to next class being called

        current_scene.enter()


class Death(Scene):

    quips = [
        "You've ruined it for everyone you failure!",
        "Try harder next time, bozo!",
        "Useless failure, good die!",
    ]

    def enter(self):
        print(Death.quips[randint(0,2)])
        exit(1)


class Croydon(Scene):

    def enter(self):
        print(dedent("""
            You, Rambo, have been summoned into London to save the city from all kinds of
            criminals. Your first stop is a mysterious South London district
            called Croydon. There are bats flying around the high street and crime
            in every nook and cranny. The roadmen plague Croydon, it is your mission to defeat
            them. They stand on the high street in their black sportswear gear and menacing
            faces. You must defeat them. Do you?
            a: Tell a joke
            b: Stab them
            c: Sneak behind them and pull their pants down
            """))

        action = input("> ")

        if action == "a":
            print(dedent("""
                You walk up to them and tell your best joke. They reply with a 'wag1
                for this yute' and stab you up.
                """))

            return 'death'

        elif action == "b":
            print(dedent("""
                You run up to the group and charge with a knife, they see you
                coming and each whip out a samurai sword from their back pocket and kill you
                """))

            return 'death'

        elif action == "c":
            print(dedent("""
                You slowly sneak up behind the head roadman and pull his pants down revealing
                a micropenis. The leader is horrified and freezes in shock. His possy lose all
                respect for him and run away. The Croydon roadmen are defeated!
                """))

            return 'clapham'

        else:
            print("Please input a requested option.")

            return 'croydon'


class Clapham(Scene):

    def enter(self):
        print(dedent("""
            You get on the tube and head for a short journey north into Clapham. A very contrasting
            challenge now awaits you. You step off the train at Clapham junction and
            immediately are struck with the distinct whiff of craft beer, avocado
            and privilege. Your phone buzzes with the mission. 'Exterminate the yuppies!'
            You google what a yuppy is and when finding out you burst into a rage,
            all the motivation to kill is with you. How do you complete your mission?
            a: Attack every yuppy in sight with your super army skills
            b: Wait outside of town and block off all of the craft beer and
            coffee imports
            c: Blend in with the yuppies, gain their trust, then poison them
            while in a flatshare
            """))

        action = input("> ")

        if action == "a":
            print(dedent("""
                Your rage turns into violence. You attack every yuppy in sight,
                but they group together and hurl avocado seed bullets at you,
                knocking you unconscious.
                """))

            return 'death'

        elif action == "b":
            print(dedent("""
                After a long mission, the yuppies in Clapham begin to die of thirst. Some
                die on the streets, others retun back to their wealthy upperclass
                villages in middle England. The yuppies are defeated.
                """))

            return 'hounslow'

        elif action == "c":
            print(dedent("""
                You move in with a group, but they become suspicious and google the name
                Rambo. They shit themselves and call the police.
                """))

            return 'death'

        else:
            print("Please input a requested option.")

            return 'clapham'


class Hounslow(Scene):

    def enter(self):
        print(dedent("""
            You travel to west london in the back of a cab. You ask the cab driver to
            take you to Hounslow and he says: 'are you sure?', to which you pause and
            question your fate...
            'I guess' you unwillingly reply.
            Hounslow is home to the Albanian mafia, big players in the cocaine industry
            in London. You have 1 day to defeat them. What do you do?
            a: Summon Chabuddy G, resident Hounslow legend to take them on
            b: Go full on Rambo with them and go on a killing spree
            c: Offer them some poisoned Albanian tea
            """))

        action = input("> ")

        if action == "a":
            print(dedent("""
                You call our for Chabuddy, within 10 seconds you hear screeching, it
                is a white Merc van hurtling around the corner. Chabuddy jumps out the
                van. He tells you to take all of the peanut dust and make the Albanians
                choke. It is successful and he rides off into the distance
                """))

            return 'hakkasan'

        elif action == "b":
            print(dedent("""
                The attack starts well, you go on a killing streak defeating 90% of
                the mafia. The big boss is Rambo 2.0 and he kills you
                """))

            return 'death'

        elif action == "c":
            print(dedent("""
                You befriend the Albanians, and eventually enough to invite them
                your hotel room to offer them the poisoned tea. As one of them
                takes a sip, he immediately spits it out and realises it is
                poisoned. It turns out that rat poison has a taste. Him
                and his boys kills you and throws you out the window.
                """))

            return 'death'

        else:
            print("Please input a requested option.")

            return 'hounslow'


class Hakkasan(Scene):

    def enter(self):
        print(dedent("""
            You ask Chabuddy on a date to Hakkasan and he accepts. You wine and
            dine him all night. The bill comes and you offer to pay, however,
            when you go to put your pin in you can't remember the last digit of
            your pin code. If you don't pay, you will have blown it with Chabuddy.
            Your pin code is 938...? You have 3 guesses before the card is blocked
            and your mission has failed.
            """))

        pin = rndm_no_gen()
        guess = input("> ")
        guesses = 0

        while guess != pin and guesses < 2:
            print("Please try again.")
            guesses += 1
            guess = input("> ")

        if guess == pin and guesses < 3:
            print("Congratulations! The bill is paid for and you sleep with Chabuddy!")
            return 'finished'

        else:
            print(dedent("""
                BEEEP BEEEP! CARD DECLINED. Chabuddy runs off and you never see
                him again
                """))
            return 'death'


class Finished(Scene):

    def enter(self):
        print("You won, your mission is complete!")
        return 'finished'


class Map(object):
# Creates a dictionary of key: value pairs
    scenes = {
        'croydon': Croydon(),
        'clapham': Clapham(),
        'hounslow': Hounslow(),
        'hakkasan': Hakkasan(),
        'death': Death(),
        'finished': Finished(),
    }

# Start_scene object is instantiated when Map class is called
    def __init__(self, start_scene):
        self.start_scene = start_scene

# Returns the value (Class) from scenes when a scene_name is called
    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

# Returns the value (Class) from scenes when the start_scene is the argument
    def opening_scene(self):
        return self.next_scene(self.start_scene)


# Creates an instance of the Map class with the 'croydon' argument
a_map = Map('croydon')
# Creates an instance of the Engine class with a_map as an argument
a_game = Engine(a_map)
# Calls the play method on the Engine class with a_map as an argument
a_game.play()
