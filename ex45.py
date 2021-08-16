from sys import exit
from random import randint
from textwrap import dedent



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
            "You died. You kind of suck pretty badly at this.",
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
        print("""As you keep moving forward through the mysterious cave, 
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
            of earshot, speaking in hushed whispers.\n\tWhen 
            kdfkfdkd""")


class MovingForwardSeparated(Scene):

    def enter(self):
        pass

class WaterInsanity(Scene):

    def enter(self):
        pass

class Escape(Scene):

    def enter(self):
        pass

class Cave(object):

    scenes = {
        'mouth_of_cave': MouthOfCave(),
        'hundred_feet_down': HundredFeetDown(),
        'the_injury': TheInjury(),
        'moving_forward_separated': MovingForwardSeparated(),
        'water_insanity': WaterInsanity(),
        'escape': Escape(),
        'death': Death(),
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

