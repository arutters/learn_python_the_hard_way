from sys import exit
from random import randint
from textwrap import dedent

# If reading this please dont judge this ugly rough draft

class Scene(object):

    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement().")
        exit(1)

class Walk(object):

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

    quips = [ "You should've tried harder.",
            "You died. Job not well done.",
            "You died, and you'll be lucky if rescuers ever find your body."
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)

class MouthOfCave(Scene):

    def enter(self):
        print(dedent("""
            As you walk through the forest and its thick collection of bushes and trees,
            up ahead you see a large opening in part of the rock formation. It looks like
            a cave. 

            Do you follow them inside and explore or stay in the woods and go back the way you came?
             """))
            
        action = input("* follow them\n* turn around\n> ")

        if action == "follow them":
            print(dedent("""
                You follow the rest of your group quickly, so as not to get left
                behind or lost.
                """))
            return 'hundred_feet_down'
        elif action == "turn around":
            print(dedent("""
                Your friends make fun of you as they walk into the cave without
                you. You turn around to start walking back through the forest the 
                way you came. Along the way you encounter a bear who kills and 
                eats you.
                """))
            return 'death'
        else: 
            print("DOES NOT COMPUTE.")
            return 'mouth_of_cave'

class HundredFeetDown(Scene):

    def enter(self):
        print(dedent("""
            You and the group walk for miles into the cave without really thinking about
            the distance into the Earth you are walking.

            You all stop to take a snack break and to rest for a moment. You look in
            awe around you at the magnificent beauty of the cave that was formed 
            millions of years ago. 

            Suddenly you look over and see your friend leaning on a boulder, but it 
            shifts, causing all of the surrounding ones to shift as well. The only
            exit is starting to close off right before your eyes and there is nothing
            you can do to stop it. 

            After a moment of serious panic, you all realize that you are going 
            to have to find another way out. 

            Do you try to move the rocks blocking the exit, or move onwards in hopes
            there is another exit along the way?
            """))

        action = input("* move the rocks\n* keep moving\n> ")

        if action == "move the rocks":
            print(dedent("""
                Your friends help you try to move the rocks, but everytime you are
                able to move one rock, another falls into its place. You keep trying
                until your hands are bloody from the jagged edges of rock, and
                you all starve to death.
                """))
            return 'death'
        elif action == "keep moving":
            return 'the_injury'
        else:
            print("A cut on your leg you hadn't noticed before gets infected and kills you.")
            return 'mouth_of_cave'

class TheInjury(Scene):

    def enter(self):
        print("""\tAs you keep moving forward through the mysterious cave, 
            you find that the path seems to become super uneven. Thinking
            nothing of it, you keep trecking along.\n\t
            Suddenly in a small mistep, you fall hard on the ground. 
            You scream in excrutiating pain as you look down at your throbbing
            leg where you can see part of your bone protruding.\n\t
            Your friends who are a little bit ahead of you come rushing back
            with a nearly useless first aid kit which only contains band-aids.\n\t
            Your friends do their best to set your leg back to the position it's
            supposed to be in-causing even more pain-and wrap it with the torn 
            shirt of one of your buddies.\n\t
            Knowing that you are unable to walk, you see them huddled just out 
            of earshot, speaking in hushed whispers.\n\tSuddenly you notice how
            silent everyone has become. They start to make their way back to you
            and tell you that they think their only change of survival will be
            if they leave you behind, and keep moving forward. They justify by
            saying that if they get out, they will get help to come back for you.\n\t
            In a state of shock you just say, 'OK'.\n\t As they start to walk away, you 
            figure you have to make a gameplan for yourself to get out. 
            \n\t Once you muster up the strength, do you start to crawl forward, or
            just sit there and hope they actually get out and send for help?
            """)
        action = input("* crawl\n* wait\n> ")

        if action == "crawl":
            return 'moving_forward_separated'
        elif action == "wait":
            print("You sit and wait for what feels like an eternity, and die of starvation and dehydration.")
            return 'death'
        else:
            return 'death'


class MovingForwardSeparated(Scene):

    def enter(self):
        print("""
            As you crawl across the jagged rocks and uneven surface, 
            your hands start to become rough and bloodied. The combination
            of your hands, leg, and your thirst becomes almost too much
            for you to handle. 
            You stop to take a little break and rest against the side of 
            cave. When you lean against it, you feel your clothes becoming 
            wet. It seems like water is lining the cave. You get the idea
            to lick the 'water' off of the walls to quench your thirst.\n
            Should you do it?
            """)
        action = input("* yes\n* no\n> ")

        if action == "yes":
            return 'water_insanity'
        elif action == "no":
            print("As you sit there your eyes become heavy and everything goes to black")
            return 'death'
        else: 
            return 'death'

class WaterInsanity(Scene):

    def enter(self):
        print("""
            As you are licking as much of the water off of the
            wall, it actually is starting to make you feel better.
            As you start to regain a little bit of strength, you 
            notice that there are actually two paths ahead of you.
            It appears that there is light at the end of one of them.
            \nDo you choose the path with the light, or the other one? 
            """)

        action = input("* the light\n* the other way\n> ")

        if action == "the light":
            print("""You feel determination and adreline soaring through your
            body as you move closer to the light. Soon you see that it isn't 
            in fact the exit, but what seems like a bioluminescent algae. As 
            you notice this, your vision starts to become blurred, and soon
            everything turns to black. """)
            return 'death'
        elif action == "the other way":
            return 'escape'
        else:
            return 'death'

class Escape(Scene):

    def enter(self):
        print("""After what feels like miles of crawling on the 
            rocky floor, you feel an unexpected slight breeze 
            crawl across your skin. That's when you look up and start to see
            the moonlight coming in from an opening just big enough for
            you to squeeze through. You ready the flare that you've kept on
            you the entire time, and as you are about to pull the trigger,
            you hear your friends calling for help from behind you in the cave.
            Do you try to go back and help them even though you may not make
            it, or do you shoot the flare and wait for help?
            """)
        action = input("* shoot flare\n* friends\n> ")

        if action == "shoot flare":
            print("""You ignore their cries for help and shoot the flare.
                You wait and wait and wait some more. Finally, you see
                a helicopter above you.\nYou have been rescued and live to 
                see another day.""")
            return 'finished'
            
        elif action == "friends":
            print("""You try your best to make your way back into the cave to
                help your friends, but it's no use. It takes up what little
                energy you had left, and you bleed out before you are able to
                get to them.""")
            return 'death'
        else:
            return 'death'

class Finished(Scene):
    def enter(self):
        print("Congrats, you won!")


class Cave(object):

    scenes = {
        'mouth_of_cave': MouthOfCave(),
        'hundred_feet_down': HundredFeetDown(),
        'the_injury': TheInjury(),
        'moving_forward_separated': MovingForwardSeparated(),
        'water_insanity': WaterInsanity(),
        'escape': Escape(),
        'death': Death(),
        'finished': Finished(),
    }
    
    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Cave.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_cave = Cave('mouth_of_cave')
a_game = Walk(a_cave)
a_game.play()

