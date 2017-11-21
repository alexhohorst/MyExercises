name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
inches_per_centimeters = 2.54
pounds_per_kilo = 0.45359

print "Let's talk about %s." % name
print "He's %d centimeters tall." % (height * inches_per_centimeters)
print "He's %d kilograms heavy." % (weight * pounds_per_kilo)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

print "If I add %d, %s and %d I get %d." % (
age, height, weight, age + height + weight)
