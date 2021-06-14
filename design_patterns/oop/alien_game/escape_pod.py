from random import randint

from ObjectOriented.AlienGame import Scene


class EscapePod(Scene):
    @staticmethod
    def enter():
        print("You rush through the ship desperately trying to make it to")
        print("the escape pod before the whole ship explodes.  It seems like")
        print("hardly any Gothons are on the ship, so your run is clear of")
        print("interference.  You get to the chamber with the escape pods, and")
        print("now need to pick one to take.  Some of them could be damaged")
        print("but you don't have time to look.  There's 5 pods, which one")
        print("do you take?")

        good_pod = randint(1, 5)
        guess = input("[pod #]> ")

        if int(guess) != good_pod:
            print("You jump into pod %s and hit the eject button." % guess)
            print("The pod escapes out into the void of space, then")
            print("implodes as the hull ruptures, crushing your body")
            print("into jam jelly.")
            return 'death'
        else:
            print("You jump into pod %s and hit the eject button." % guess)
            print("The pod easily slides out into space heading to")
            print("the planet below.  As it flies to the planet, you look")
            print("back and see your ship implode then explode like a")
            print("bright star, taking out the Gothon ship at the same")
            print("time.  You won!")

            return 'finished'
