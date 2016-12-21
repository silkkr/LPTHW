class Scene(object):
    def __init__(self, title, urlname, description):
        self.title = title
        self.urlname = urlname
        self.description = description
        self.paths = {}

    def go(self, direction):
        default_direction = None
        if '*' in self.paths.keys():
            default_direction = self.paths.get('*')
        return self.paths.get(direction, default_direction)

    def add_paths(self, paths):
        self.paths.update(paths)

# Create the scenes of the game
outside_bar = Scene("Welcome to Karaoke Hell", "outside_bar",
"""
You were having a pleasant Friday evening with friends, when suddenly they drag
you to a Thai Karaoke Bar! Oh no!!! Your mission tonight is to get back home
safely, not get beaten up or worse.
First, you need to get through the bouncer Odin.

Odin: Did you drink before you came here, yes or no?\n""")

inside_bar = Scene("Inside Bar", "inside_bar",
"""
You've now entered the bar. A drunk lady is singing Abba.\n
Your friends urge you to sing along. Fill in the missing lyrics!\n\n
You are the dancing queen, young and ____, only seventeen
""")

the_counter = Scene("The Counter", "the_counter",
"""
You're now at the counter. Do you want to buy a drink?
""")

the_hell = Scene("The Hell", "the_hell",
"""
As you hang out in the bar counter, an elderly couple notices you. You intrigue
them with your vitality. Sooner than you realize, you have been kidnapped to a
V.I.P. old people's karaoke lounge out back, and you're holding a Pina Colada.

Suddenly, your favorite song Take on Me by A-ha starts to play, and you faint
from excitement. Ethel has bad eyesight, thinks you are 90 and having a heart
attack, and feeds you two of her nitros. Gulp!

You had Ethel's nitros and DIED! Now you are in the actual hell!

        The Devil: Bwahaha, that karaoke bar is providing me with more souls
        than any other establishment I own!! I will grant you one opportunity to
        return back to earth. To regain your soul, you must sing this karaoke song!

        Fill in the blanks:
        Forever young, I want to be forever young.
        Do you really want to ____ _______? Forever, and ever
""")

biker_death = Scene("O-oh!", "biker_death",
"""
You just butchered ABBA! A giant biker meat mountain from MC ABBA overhears you,
sheds a tear of anger, drags you to the back alley and gives you the beating of
your life. You lost.
""")

stag_death = Scene("That was a mistake...", "stag_death",
"""
You loiter by the counter without a drink and encounter an English stag party!

"Oi mate, innit a bit fairy to be prissying around without a beer in ye hand?"

That was the last thing you heard and then a fist hit your face. You lost.
""")

the_end_winner = Scene("The Winner Takes It All", "the_end_winner",
"""
Wow! What a night! Well done!
""")

the_end_loser = Scene("...", "the_end_loser",
"""
Oh no. Your soul has perished, permanently. You will spend eternity in an even
worse karaoke bar. I'm sorry. You lost.
""")

# Define the action commands available in each Scene
the_hell.add_paths({
    'live forever': the_end_winner,
    '*': the_end_loser
})

the_counter.add_paths({
    'no': stag_death,
    'yes': the_hell
})

inside_bar.add_paths({
    'sweet': the_counter,
    '*': biker_death
})

outside_bar.add_paths({
    'yes': inside_bar,
    'no': inside_bar
})


# Make some useful variables to be used in the web application
SCENES = {
    outside_bar.urlname: outside_bar,
    inside_bar.urlname: inside_bar,
    the_counter.urlname : the_counter,
    the_hell.urlname : the_hell,
    the_end_winner.urlname : the_end_winner,
    the_end_loser.urlname : the_end_loser,
    biker_death.urlname : biker_death,
    stag_death.urlname : stag_death,
}
START = outside_bar
