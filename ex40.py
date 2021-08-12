# modules - a python file with some functions or variables in it
            # - you import that file
            # - you can access the functioned or variable in that moduke with the . (dot) operator
class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics
    
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happier_than_ever = Song(["When I'm away from you",
                            "I'm happier than ever"])


happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song() 

happier_than_ever.sing_me_a_song()


