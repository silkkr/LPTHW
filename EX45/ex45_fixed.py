import sys
from sys import exit
from time import sleep


class Scene (object):

    def enter(self):
        exit(1)


class Engine(object):

        def __init__(self, scene_map):
            self.scene_map = scene_map

        def play(self):
            current_scene = self.scene_map.opening_scene()
            last_scene = self.scene_map.next_scene('finished')

            while current_scene != last_scene:
                next_scene_name = current_scene.enter()
                current_scene = self.scene_map.next_scene(next_scene_name)

            current_scene.enter()


class Death(Scene):
    def enter(self):
        print "Well that was horrible."
        exit()


class Start(Scene):
    def enter(self):
        print """

        ,--.   ,--.,------.,--.    ,-----. ,-----. ,--.   ,--.,------.
        |  |   |  ||  .---'|  |   '  .--./'  .-.  '|   `.'   ||  .---'
        |  |.'.|  ||  `--, |  |   |  |    |  | |  ||  |'.'|  ||  `--,
        |   ,'.   ||  `---.|  '--.'  '--_''  '-'  '|  |   |  ||  `---.
        '--'   '--'`------'`-----' `-----' `-----' `--'   `--'`------'
                )          ,--------. ,-----.              )
               ) \     )   '--.  .--''  .-.  '      )     ) '
              / ) (   ) \     |  |   |  | |  |     ) \   / ) (
              \(_)/  / ) (    |  |   '  '-'  '    / ) (  \(_)/
                     \(_)/    `--'    `-----'     \(_)/
        ,--. ,--.  ,---.  ,------.   ,---.   ,-----. ,--. ,--.,------.
        |  .'   / /  O  \ |  .--. ' /  O  \ '  .-.  '|  .'   /|  .---'
        |  .   ' |  .-.  ||  '--'.'|  .-.  ||  | |  ||  .   ' |  `--,
        |  |\   \|  | |  ||  |\  \ |  | |  |'  '-'  '|  |\   \|  `---.
        `--' '--'`--' `--'`--' '--'`--' `--' `-----' `--' '--'`------'
          )           ,--.  ,--.,------.,--.   ,--.               )
         ) \     )    |  '--'  ||  .---'|  |   |  |        )     ) '
        / ) (   ) \   |  .--.  ||  `--, |  |   |  |       ) \   / ) (
        \(_)/  / ) (  |  |  |  ||  `---.|  '--.|  '--.   / ) (  \(_)/
               \(_)/  `--'  `--'`------'`-----'`-----'   \(_)/"""


        start_words= """
You were having a pleasant Friday evening with friends, when suddenly they drag
you to a Thai Karaoke Bar! Oh no!!! Your mission tonight is to get back home
safely, not get beaten up or worse.
First, you need to get through the bouncer Odin.

        Odin: How much have you had to drink?\n"""

        for char in start_words:
            sleep(0.06)
            sys.stdout.write(char)
            sys.stdout.flush()

        choice = raw_input("\tYou: ")

        if choice == "not much":
            print "\tOdin: Huh, better get your drink on! Welcome!"
            return 'bar'

        else:
            print "\tOdin: Hmm, ok. I'll be watching you.."
            return 'bar'


class Bar(Scene):
    def enter(self):
        print "\nYou've now entered the bar. A drunk lady is singing Abba."
        print "Your friends urge you to sing along. Fill in the missing lyrics!"
        print "\n\t\033[1mYou are the dancing queen,\n\tyoung and ____,\n\tonly seventeen\033[0m"

        choice = raw_input("\nFill the blank: ")

        if choice == "sweet":
            print "\nAbba abba! That's right! You've been here before!"
            return 'counter'

        else:
            print "\nOh no, try again!"

            choice = raw_input("You: ")

            if choice == "sweet":
                print "\nWell finally! Let's go get a drink!"
                return 'counter'

            else:
                print "Oh no. You were thrown out cause you suck at karaoke."
                return 'death'


class Counter(Scene):
    def enter(self):
        print "\nYou're now at the counter. Do you want to buy a drink?"
        option = raw_input("You: ")

        if option == "yes":
            return 'hell'

        elif option == "no":
            print "\nI have a feeling you'll regret not drinking more.."
            return 'hell'

        else:
            print "\nO-o! A biker sees you loitering by the counter and wants to"
            print "pick up a fight. You have to escape home and ditch your friends."
            return 'death'


class Hell(Scene):
    def enter(self):
        start_words= """
As you hang out in the bar counter, an elderly couple notices you. You intrigue
them with your vitality. Sooner than you realize, you have been kidnapped to a
V.I.P. old people's karaoke lounge out back, and you're holding a Pina Colada.

Suddenly, your favorite song Take on Me by A-ha starts to play, and you faint
from excitement. Ethel has bad eyesight, thinks you are 90 and having a heart
attack, and feeds you two of her nitros. Gulp!

You had Ethel's nitros and DIED! Now you are in the actual hell!

        The Devil: Bwahaha, that karaoke bar is providing me with more souls
        than any other establishment I own!!
        I will grant you one opportunity to return back to earth. To regain your
        soul, you must sing this karaoke song!"""
        for char in start_words:
            sleep(0.06)
            sys.stdout.write(char)
            sys.stdout.flush()
        return 'swansong'


class Swansong(Scene):
    def enter(self):
        print "\n\n\t\033[1mForever young,\n\tI want to be forever young."
        print "\tDo you really want to ____ _______? Forever, and ever\033[0m"

        choice = raw_input("\n\tFill the blanks: ")

        if choice == "live forever":
            print "\n\tThe Devil: Arrgghh! You have broken my spell! I shall"
            print "send you home!\n"
            return 'finished'

        else:
            print "\nOh no. You're dead forever."
            return 'death'


class Finished(Scene):

    def enter(self):
        print "Wow! What a night! Well done!"
        return 'end'


class Map(object):

    scenes = {
        'start': Start(),
        'bar': Bar(),
        'counter': Counter(),
        'hell': Hell(),
        'swansong': Swansong(),
        'death': Death(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('start')
a_game = Engine(a_map)
a_game.play()
