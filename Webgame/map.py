class Scene(object):

    def __init__(self, title, urlname, description, img, m_choice):
        self.title = title
        self.urlname = urlname
        self.description = description
        self.paths = {}
        self.img = img
        self.m_choice = m_choice


    def go(self, direction):
        default_direction = None
        if '*' in self.paths.keys():
            default_direction = self.paths.get('*')
        return  self.paths.get(direction, default_direction)


    def add_paths(self, paths):
        self.paths.update(paths)


opening_scene = Scene("Welcome", "opening_scene",
"""
HELP! We are in space! ... And we are stuck!
Even though you are enjoying the view of the earth, we really need to go
back to earth! Look around you...
It seems like there are no more than two options.
You can either jump onto a spaceship or try to scream for help.
Or - of course - you could simply chose to not care at all and take a nap...
""", "/static/img/space1.jpg", 1)

space_ship = Scene("Space ship", "space_ship",
"""
Wow, fella! Good jump! Looks like we now have to get further into this spaceship.
Maybe this is our chance to go back to earth!
But how?
Hmm... looks like there's a door. It's locked with a code...
Can you guess it?
""", "/static/img/door.jpg", 0)

space_room = Scene("Space room", "space_room",
"""
You run and run and run, expecting to find someone or something to help you.
After crossing a lot of bizarre-looking things and ducking one or the other meteroite,
you can spot a spaceshuttle in the distance. You start to sprint.

After you got there, there are two drivers in astronaut suits.
'I need all of your information to bring you back down to earth', he said.
QUICK! Fill out this form! The progress bar will tell you have far you've come.
With every given answer we will come closer to earth.
""", "/static/img/space1.jpg", 1)

way_earth = Scene("Way to earth", "way_earth",
"""
GREAT CHOICE! You almost made it!
You are on your way back to earth now. The spaceshuttle seems to get even faster and faster...
You start to talk to the astronauts, who turn out to be Neil Armstrong and Sigmund Jaehn.
Two of the astronauts who have been on the moon!! They seem pretty happy with your performance
in space so far so they offer to take you home to their homecountry.
Well... Which country do you want to go to?
""", "/static/img/space1.jpg", 1)

back_germany = Scene("Willkommen zuhause", "back_germany",
"""
Willkommen zuhause mein Freund! Glad to have you back on earth!
""", "/static/img/germany.jpg", 2)

back_USA = Scene("Welcome back, mister!", "back_USA",
"""
Welcome home mister! Hope you had a nice time abroad.
""", "/static/img/usa.jpg", 2)

scream_help = Scene("Scream for help", "scream_help",
"""
Miracles happen... Somewhere far, far away you hear someone answering you.
But you just cannot understand what he (or she?) is saying. You run around, looking for
anything to make the sounds louder. You find a mp3 cord, a microphone and a banana.
What do you use?
""", "/static/img/space1.jpg", 1)

death = Scene("Death...", "death",
"""
Bababaaaam... I am sorry but it takes more than this to be a real astronaut!
Try again maybe?
""", "/static/img/Rakete-Animation.jpg", 0)

# Define the action commands available in each scene
opening_scene.add_paths({
    'Jump': space_ship,
    'Scream for help': scream_help,
    'Take a nap': death,
})
space_ship.add_paths({
    '123': space_room,
    '*': death
})

scream_help.add_paths({
    'Mp3 cord': way_earth,
    'Microphone': way_earth,
    'Banana': death
})

space_room.add_paths({
    'Submit': way_earth
})

way_earth.add_paths({
    'Germany': back_germany,
    'USA': back_USA
})


# Make some useful variables to be used in the web application
SCENES = {
    opening_scene.urlname : opening_scene,
    scream_help.urlname : scream_help,
    space_room.urlname : space_room,
    space_ship.urlname : space_ship,
    way_earth.urlname : way_earth,
    back_USA.urlname : back_USA,
    back_germany.urlname : back_germany,
    death.urlname : death
}
START = opening_scene
