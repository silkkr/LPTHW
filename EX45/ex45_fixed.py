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


        start_words= """\nYou were having a pleasant Friday evening with friends, when suddenly they drag you to a Thai Karaoke Bar! Oh no!!! Your mission tonight is to not insult your  friends, get back home safely, not get beaten up or lose your money.\nFirst, you need to get through the bouncer Odin.\n\n\tOdin:
        How much have you had to drink?\n"""

        for char in start_words:
            sleep(0.06)
            sys.stdout.write(char)
            sys.stdout.flush()

        choice = raw_input("\tYou: ")

        if choice == "nothing":
            print "\tOdin: Huh, better get your drink on! Welcome!"
            return 'bar'

        else:
            print "\tOdin: Hmm, ok. I'll be watching you.."
            return 'bar'


class Bar(Scene):
    def enter(self):
        print "\nYou've now entered the bar. A drunk lady is singing Abba. Your friends urge you to sing along. Fill in the missing lyrics!\n"
        print "\t\033[1mYou are the dancing queen,\n\tyoung and ____, only seventeen\033[0m"

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
                print "Oh no. You were thrown away from bar cause you suck at karaoke."
                return 'death'

class Counter(Scene):
    def enter(self):
        print "\nYou're now at the counter. Do you want to buy a drink?"
        option = raw_input("You: ")

        if option == "yes":
            return 'hell'

        elif option == "no":
            print "I have a feeling you'll regret not drinking more.."
            return 'hell'

        else:
            print "O-o! A biker sees you loitering by the counter and wants to pick up a fight. You have to escape home and ditch your friends."
            return 'death'


class Hell(Scene):
    def enter(self):
        start_words= """\nAs you hang out in the bar counter, an elderly couple notices you. You intrigue them with your vitality. Sooner than you realize, you have been kidnapped to a\nprivate V.I.P. karaoke lounge out back, and you're holding a Pina Colada.\n\nSuddenly, your favorite song Take on Me by A-ha starts to play, and you faint\nfrom excitement. Ethel has bad eyesight, thinks you are 90 and having a heart\nattack, and feeds you two of her nitros. Gulp!\n\nYou had Ethel's nitros and DIED! Now you are in the actual hell!\n\n\tThe Devil: Bwahaha, that karaoke bar is providing me with more souls\n\tthan any other establishment I own!!\n\tI will grant you one opportunity to return back to earth. To regain your \tsoul, you must sing this karaoke song!"""
        for char in start_words:
            sleep(0.06)
            sys.stdout.write(char)
            sys.stdout.flush()
        return 'swansong'

class Swansong(Scene):
    def enter(self):
        print "\n\n\t\033[1mForever young,\n\tI want to be forever young.\n\tDo you really want to ____ _______? Forever, and ever\033[0m"

        choice = raw_input("\n\tFill the blanks: ")

        if choice == "live forever":
            print "\n\tThe Devil: Arrgghh! You have broken my spell! I shall send you home!"
            return 'finished'

        else:
            print "Oh no. You're dead forever."
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
