x = "There are %d types of people." % 10 #assigning the variable
binary = "binary" #assigning the variable
do_not = "don't" #assigning the variable
y = "Those who know %s and those who %s." % (binary, do_not) #TWO STRINGS INSIDE A STRING

print x #print: There are only types of people
print y #print: those who know binary and those who don't.

print "I said: %r." % x #STRING INSIDE OF A STRING
print "I also said: '%s'." % y #one string inside of a string

hilarious = False #assigning variable
joke_evalutation = "Isn't that joke so funny?! %r" #prints: isn't that joke so funny? false"

print joke_evalutation % hilarious

w = "This is the left side of..." #assigning
e = "a string with a right side." #assigning

print w + e
