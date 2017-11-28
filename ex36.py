from sys import exit

def begin():
	print "It's thanksgiving break."
	print "Let's use this time to do something to get to know each other..."
	print "First off, what's your name?"

	yourName = raw_input("> ")
	print "Hello", yourName,"!"
	print "Would you rather dive into Black Friday's madness and go shopping or spend time with your family?"

	next = raw_input("> ")

	if next == "shopping":
		thrift_shop ()
	elif next == "family":
		family_time ()
	else:
		exit("You lazy piece of turkey.")

def thrift_shop():
	print "Yay, let's do some thrift shopping. Whatwhatwhat..."
	print "I'm gonna pop some tags."
	print "Only got ..."
	print "Well - how much dollar you got in your pocket?"

	next = raw_input("> ")

	if next == "20":
		print "YES! This is f*cking awesome."
		print "Congrats! You have the potential to be my new shopping buddy."
		print "Here we go, off to the thrift shop!"
		store()
	else:
		print "Oh come on, we all know some Macklemore. You are no fun."
		print "But now that we are already here, let's go back to the family."
		family_time()

def store():
	print "Now let's get serious."
	print "How much money would you like to spend?"

	next = int(raw_input("> "))

	if next <5:
		print "Oh honey, you should not make false economies... Go save some money and come back another time!"
		exit(0)
	elif next>5:
		print "Yup, we can work with that."
		outfits()
	else:
		print "Instead of learning lyrics, you should probably do some maths dude!"
		exit()


def outfits():
	print "Now that we got the money problem solved, it is time to find an outfit."
	print "Which outfit would you like to chose?"
	print "\tThis one right here is really sassy."
	print "\n\t\tOr you could go with these fancy pants..."
	print "\n\t\t\t...while this outfit one is rather boring."
	print "Now which one do you chose?"

	next = raw_input("> ")
	if next == "sassy":
		print "Great choice!"
		leaving()

	elif next == "fancy pants":
		print "I'm sure this will look amazing on you."
		leaving()

	elif next == "boring":
		print "Yeaaahhhhhhhh... You might know Macklemore but that's pretty much all the cool stuff about you. Bummer."
		leaving()

def leaving():
	print "Anyway - now that we decided (man, you take quite some time time!) we have to get in line."
	print "And oh man, that line is long!"
	print "Let's try to make some people leave. Yeah I know, that's embarrassing but I know you want to leave as badly as I do."
	print "Do you want to 1. sing to make them flee, 2. rub and run away or 3. haughty cutting the line?"
	longLine = False

	while True:
		next = raw_input("> ")

		if next == "sing":
			print "Well, now we got all eyes on us, but ain't nobody moving..."
			longLine = True
		elif next == "rub":
			print "EXCUSE ME! THAT WAS A JOKE!"
			longLine = True
		elif next == "cutting the line":
			print "Oh you're so German! Well... at least it worked. On we go - back to our families!"
			longLine = False
			family_time()
		else:
			print "What? Sorry. Tell me again, I didn't hear you."
			longLine = True

def family_time():
	print "First, tell me a little bit about your family."
	print "On a scale from 1 to 10, how fun is your family?"

	next = int(raw_input("> "))
	if next <= 5 and next >= 1:
		print "You know you can't pick your family, but your friends right... Thanks for playing anyways!"
		exit(0)

	elif  6<= next <= 10:
		print "Then stop playing this stupid game and go enjoy the time you got!"
		exit(0)

	else:
		print "Never heard of a scale? 1-10 please!"

begin()
