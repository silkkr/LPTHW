from sys import exit

print """
 *               *               *               *                *
.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:.

      *   x   Welcome to the Christmas Present Machine!     x   *

.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:.
 *               *               *               *                *
"""


def female_gift():
    print "\nWhich one is she?"
    print "\nA house mouse or an adventurer?\n"

    choice = raw_input("> ")

    if choice == "house mouse" or choice == "a house mouse":
        female_gift_housemouse()
    elif choice == "adventurer" or choice == "an adventurer":
        female_gift_adventurer()
    else:
        print "\nNaughty, naughty! You didn't answer correctly! Don't make Santa mad, the anagram Satan is NOT a coincidence! Pick one of the options.\n"
        female_gift()


def female_gift_housemouse():
    print "\nIs she more into beauty, books or house decor?\n"

    choice = raw_input("> ")

    if choice == "beauty":
        print "\nGet her an Aquis Hair Towel and a Patyka Body Wash in your favourite scent.\n"
        christmas_wish()
    elif choice == "books":
        print "\nGet her The White Album by Joan Didion! You'll look cool.\n"
        christmas_wish()
    elif choice == "house decor":
        print "\nGet her a scented candle! Fornasetti if you want to spend, Diptyque if you want to skimp. Don't forget to make a DIY Christmas card to go with it.\n  "
        christmas_wish()
    else:
        print "\nNaughty, naughty! You didn't answer correctly! Don't make Santa mad, the anagram Satan is NOT a coincidence! Pick one of the options.\n"
        female_gift_housemouse()


def female_gift_adventurer():
    print "\nIs she more into travel, sports or sex?\n"

    choice = raw_input("> ")

    if choice == "sports":
        print "\nGet her a Lulu Lemon Run Ways Duffel Sports bag.\n"
        christmas_wish()
    elif choice == "sex":
        print "\nGet her the Ooh Her name is Rio set by Je Joue. Also give hot kisses.\n"
        christmas_wish()
    elif choice == "travel":
        travel_selection()
    else:
        print "\nNaughty, naughty! You didn't answer correctly! Don't make Santa mad, the anagram Satan is NOT a coincidence! Pick one of the options.\n"
        female_gift_adventurer()


def male_gift():
    print "\nWhich one is he?"
    print "\nA house mouse or an adventurer?\n"

    choice = raw_input("> ")

    if choice == "house mouse" or choice == "a house mouse":
        male_gift_housemouse()
    elif choice == "adventurer" or choice == "an adventurer":
        male_gift_adventurer()
    else:
        print "\nNaughty, naughty! You didn't answer correctly! Don't make Santa mad, the anagram Satan is NOT a coincidence! Pick one of the options.\n"
        male_gift()


def male_gift_housemouse():
    print "\nIs he more into self care, books or kitchenware?\n"

    choice = raw_input("> ")

    if choice == "self care":
        print "\nGet him a Bulldog skincare product set! They are microbead free, paraben free,  cruelty free and smell like fresh ginger.\n"
        christmas_wish()
    elif choice == "books":
        print "\nGet him My Struggle by Knausgard! Guys love that shit.\n"
        christmas_wish()
    elif choice == "kitchenware":
        print "\nGet him a Hario coffee siphon.\n  "
        christmas_wish()
    else:
        print "\nNaughty, naughty! You didn't answer correctly! Don't make Santa mad, the anagram Satan is NOT a coincidence! Pick one of the options.\n"
        male_gift_housemouse()


def male_gift_adventurer():
    print "\nIs he more into travel, sports or sex?\n"

    choice = raw_input("> ")

    if choice == "sports":
        print "\nGet him sneakers. You can spy the size and brand from his shoe shelf.\n"
        christmas_wish()
    elif choice == "sex":
        print "\nPledge for the ethically produced & independent Four Chambers videos on Patreon for him and give the access codes inside an envelope. Also give hot kisses.\n"
        christmas_wish()
    elif choice == "travel":
        travel_selection()
    else:
        print "\nNaughty, naughty! You didn't answer correctly! Don't make Santa mad, the anagram Satan is NOT a coincidence! Pick one of the options.\n"
        male_gift_adventurer()


def other_gift():
    print "\nWhich one are they?"
    print "\nA house mouse or an adventurer?\n"

    choice = raw_input("> ")

    if choice == "house mouse" or choice == "a house mouse":
        other_gift_housemouse()
    elif choice == "adventurer" or choice == "an adventurer":
        other_gift_adventurer()
    else:
        print "\nNaughty, naughty! You didn't answer correctly! Don't make Santa mad, the anagram Satan is NOT a coincidence! Pick one of the options.\n"
        other_gift()


def other_gift_housemouse():
    print "\nAre they more into self care, books or homeware?\n"

    choice = raw_input("> ")

    if choice == "self care":
        print "\nGet them the Unnamed by Byredo, a conceptual unisex perfume.\n"
        christmas_wish()
    elif choice == "books":
        print "\nGet them A Safe Girl to Love by Casey Plett! Short stories are nice to read over the holidays.\n"
        christmas_wish()
    elif choice == "homeware":
        print "\nPamper them with hotel sheets at home! Frette if you want to spend, Brooklinen  if you want to skimp. \n  "
        christmas_wish()
    else:
        print "\nNaughty, naughty! You didn't answer correctly! Don't make Santa mad, the anagram Satan is NOT a coincidence! Pick one of the options.\n"
        male_gift_housemouse()


def other_gift_adventurer():
    print "\nAre they more into travel, sports or sex?\n"

    choice = raw_input("> ")

    if choice == "sports":
        print "\nGet them a yoga mat, yoga block and the Yogaia online yoga subscription.\n"
        christmas_wish()
    elif choice == "sex":
        print "\nGet them a gift certificate to Other Nature Berlin, the feminist, queer-oriented & eco-friendly vegan sex shop in Kreuzberg which ships from their online shop. You can get one by e-mailing them.\n"
        christmas_wish()
    elif choice == "travel":
        travel_selection()
    else:
        print "\nNaughty, naughty! You didn't answer correctly! Don't make Santa mad, the anagram Satan is NOT a coincidence! Pick one of the options.\n"
        male_gift_adventurer()


def travel_selection():
    print "\nHow much are you willing to spend?\n"

    next = raw_input("> ")

    try:
         how_much = int(next)
    except ValueError:
        print "\nNaughty, naughty! You didn't answer correctly! Don't make Santa mad, the anagram Satan is NOT a coincidence! Pick one of the options.\n"
        travel_selection()

    if how_much < 50:
        print "\nThat's not a lot! Maybe just go for a walk together or pick something else?\n"
        exit(0)
    if how_much < 100:
        print "\nPrepare a day trip to a town near by and gift the day plan in a nice envelope.\n"
        christmas_wish()
    if how_much < 200:
        print "\nBook a hotel and go out together in your own town.\n"
        christmas_wish()
    if how_much < 300:
        print "\nPlan a weekend in Berlin!\n"
        christmas_wish()
    if how_much < 700:
        print "\nTreat your SO to a weekend in Copenhagen!\n"
        christmas_wish()
    if how_much < 1200:
        print "\nBook flights for two and a villa in Andalucia!\n"
        christmas_wish()
    if how_much >= 1200:
        print "\nBook flights to New York!\n"
        christmas_wish()
    else:
        print "\nOops, can I get that in numbers only?\n"
        travel_selection()


def christmas_wish():
    print """
                  *   *  ****  ***   ***   *   *
                  ** **  *     *  *  *  *   * *
                  * * *  ***   ***   ***     *
                  *   *  *     * *   * *     *
                  *   *  ****  *  *  *  *    *

       ***   *  *  ***   *  ****  *****  *   *   **   ****   ***
      *   *  *  *  *  *  *  *       *    ** **  *  *  *      ***
      *      ****  ***   *  ****    *    * * *  ****  ****   ***
      *   *  *  *  * *   *     *    *    *   *  *  *     *    *
       ***   *  *  *  *  *  ****    *    *   *  *  *  ****    *\n
    """
    exit(0)

def start():
    print "Let's choose a gift for your significant other! \n\nNavigate through Santa's workshop by typing your choice.\n"
    print "Is your significant other...\n"
    print "a female? \n\na male? \n\nother? (why are you even asking, that's sexist & there's more than two genders  you know)\n"

    choice = raw_input("> ")

    if choice == "female" or choice == "a female":
        female_gift()
    elif choice == "male" or choice == "a male":
        male_gift()
    elif choice == "other":
        other_gift()
    else:
        exit("If you don't wanna answer properly, just buy them the Elf DVD or try again.")


start()
