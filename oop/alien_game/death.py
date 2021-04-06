from random import randint

from ObjectOriented.AlienGame import Scene


class Death(Scene):
    __quips = [
        "You died.  You kinda suck at this.",
        "Your mom would be proud...if she were smarter.",
        "Such a looser.",
        "I have a small puppy that's better at this."
    ]

    def enter(self):
        print(self.__quips[randint(0, len(self.__quips) - 1)])
        pass
