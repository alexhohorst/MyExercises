from sys import exit
from random import randint
bold = "\033[1m"
reset = "\033[0;0m"

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

class Scene (object):

    def enter(self):
        print " "
        exit (1)

class Start (Scene):
    def enter(self):
        print "Hola and hello!"
        print "Now that we have all survived the Thanksgiving madness, it's time to think about ... You guessed it right!"
        print "IT'S" + bold + " CHRISTMAS!!!" + reset
        print "So first of all... Are you already done with all your presents shopping?"
        gifts_ready = False

        while True:
            next = raw_input("> ")

            if next == "yes":
                print "Okay, enough with the lying. Nobody has all their gifts ready until midday, December 24th. Be honest already."
                print "So, let me ask you again: are you already done with ALL your presents shopping?"
                gifts_ready = True
            elif next == "no":
                gifts_ready = False
                return 'days_count'
            else:
                print "What? Sorry. Tell me again, I didn't hear you."
                gifts_ready = True

class DaysCount(Scene):
    def enter (self):
        print "YES! A kindred spirit!"
        print "So, let me try to help you."
        print "How many days do you have left to prevent an EXTREMELY embarassment handing out of presents?"

        next = int(raw_input("> "))
        if next <3:
            print "Okay what... We have some emergency right here!"
            print "Looks like you need to find a solid amount of 7 presents for people you ACTUALLY care about..."
            return 'listing'

        elif next >3:
            print "Okay, looks like you have enough time to simply run to a store to get something nice."
            print "So hurry up and try to safe this madness!"
            return 'death'

class Listing(Scene):
    def enter (self):
        print "And I know that during christmas time, everybody has some things at home. Let's see what we can do."
        list_home = "Chocolate Mandarines Speculoos Gingerbread"
        print list_home
        print "Okay, first of all: you are such a lazy person. I know you only went to the kitchen"
        print "instead of looking around in all of your rooms."
        print "So unless you wish to cram your family and friends, I'd suggest you"
        print "keep on looking. And remember... we need at least seven things! 3 more to go!"
        print "Now get your fat butt up again and look around!!!"
        print "\n\t *spongebob voice* 24 hours later..."
        print "HURRY UP DUDE. What's taking so long?"
        print "Guess I'll just take a nap until you're done. Simply scream 'HEY SANTA' when you're done!"

        next = raw_input("> ")
        if next == "HEY SANTA":
            print "FINALLY!!!!!!!"
            return 'stuff'

        else:
            print "I'm napping, alright? Just tell me when you're ready."
            return 'listing'

class Stuff(Scene):
    def enter (self):
        print "\n\t\t Let's see what else you found!"
        list_home = "Chocolate Mandarines Speculoos Gingerbread"
        print "So far we have", list_home
        stuff = list_home.split(' ')
        more_stuff = ["nice Pen", "DVD", "scented candle"]

        while len(stuff) != 7:
            next_one = more_stuff.pop()
            print "Ohhhh you found a", next_one
            stuff.append(next_one)
            print "Now you have %d gifts..." % len(stuff)

        print "YES! You got it! Now you got a beautfiul nice collection, consisting of ", stuff
        print "Yay you! Now it's time to do wrapping."
        print "But lets check if you're still with me. A little quiz. (Where's the drum roll when you need it?)"
        print "Walter Afanasieff wrote the song we all cried our eyes out to: Celine Dion's 'My heart will go on'."
        print "Buuut he also co-wrote one of the most famous christmas songs by one of the most famous divas of our time."
        print "Can you guess it?"

        next = raw_input("> ")
        if next == "all i want for christmas is you":
            print "Exactly! Now that you got that in your head for the rest of the day (you're welcome), let's move on."
            return 'wrapping'
        else:
            print "Need a hint? IIIII DONT WANT AALLLOOTT FOR CHRISTMAAAAS...."
            return 'stuff'

class Wrapping(Scene):
    def enter (self):
        print "Okay buddy, looks like we've got a problem."
        print "The wrapping paper is in the basement, but the basement is locked with a code."
        print "And guess who set the code for it...?"
        print "\t Exactly! Your mum!"
        print "And we all know: if you told your mum you still didn't have your gifts ready... Exactly. I won't even go there."
        print "It's a 4-digit code. I can tell you a little hint: What year was the song you just guessed released?"
        code = "%d%d%d%d" % (int (1), int (9), int (9), int (4))
        guess = raw_input("[keypad]> ")
        guesses = 0

        while guess != code and guesses <4:
            print "No! Try again... and don't give me that look, I won't call your mummy."
            guesses += 1
            guess = raw_input("[keypad]> ")

        if guess == code:
            print "YESSSS! No embarassing phone call with your mum! That's even better than christmas."
            return 'basement'

        else:
            print "Looks like I have to call your mum either way."
            print "I guess that's it. No christmas for you. I'm sorry."
            print "\n Okay, not really sorry. But hey - maybe next year?"
            return 'death'

class Basement(Scene):
    def enter (self):
        print "Okay, let's see what colors we have."
        colors = "Blue, Pink, Red"
        print colors
        print "Which one would you like for your gifts?"
        christmassy = False

        while True:
            choice = raw_input("> ")

            if choice == "Blue":
                print "Ever heard of christmas colors? You've done well so far, but this is definitely wrong."
                christmassy = True
            if choice == "Pink":
                print "Naw, cute. But remember this is christmas, not your baby sister's birthday party."
                christmassy = True
            if choice == "Red":
                print "Great! You found the most christmas-sy color there is."
                christmassy = False
                return 'tree'

class Tree (Scene):
    def enter (self):
        print "Okay, we have the presents, we have the wrapping paper... What else do we need?"
        print "Exactly! YOU!"
        print "\t Wait what..."
        print "Exactly! What's all the gifts, with the nicest wrapping paper, when you're not in the christmas mood?"
        print "So... tell me: "
        print "On a scale from 1 to 10, how intense is your christmas mood?"

        next = int(raw_input("> "))
        if next <= 3 and next >= 1:
            return 'death'

        if next <= 7 and next >= 4:
            print "WOW! Okay this is an even bigger emergency than the gifts-part."
            print "Here are some rules you should follow:"
            print "Put on a jelly bag cap. Put on All I want for christmas is you."
            print "Tell your neighbors you're sorry."
            print "AND NOW SING ALONG: IIII DON'T WANT ALLLOOTT FORRR CHRISTMASSS"
            print "THERE IS JUST ONE THING I NEED. I DONT CARE ABOUT THE PRESENTS UNDERNEATH THE CHRISTMAS TREEEEE..."
            print "(Alright, I'm gonna leave you right here to prevent sincere ear damages)"
            print "But now..."
            return 'end'

        if  next <= 10 and next >= 7:
            print "That's my kinda spirit! But this still needs a little boosting."
            print "Turn on some christmas music (I might have given you some suggestions along the way)"
            print "and go to this website: https://www.bbcgoodfood.com/recipes/category/christmas"
            print "Do some cooking, do some dancing along the kitchen and TADA!"
            print "Christmas mood is there! So there's only one thing left to say:"
            return 'end'

class Death (Scene):
    def enter (self):
        print "That's all you got?"
        print "Even after singing along to Mariah Carey, calling ME Santa, wrapping seven presents"
        print "And you still you're that grumpy?"
        print "I'm speechless."
        print "Well, maybe next year christmas won't come as sudden as this year (ahem)"
        print "And you can try again..."
        exit(1)

class End(Scene):
    def enter (self):
        print bold + "MERRY CHRISTMAS!" + reset + " Have a wonderful time with your beloved ones and your gifts..."
        print "And a happy new year! Pop the corks!!"
        exit(1)



class Map (object):

    scenes = {
        'Start': Start(),
        'days_count': DaysCount(),
        'wrapping': Wrapping(),
        'basement': Basement(),
        'listing': Listing(),
        'end': End(),
        'stuff': Stuff(),
        'death': Death(),
        'tree': Tree(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene (self):
        return self.next_scene(self.start_scene)

a_map = Map ('Start')
a_game = Engine(a_map)
a_game.play()
