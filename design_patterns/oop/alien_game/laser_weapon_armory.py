from random import randint

from ObjectOriented.AlienGame import Scene


class LaserWeaponArmory(Scene):

    @staticmethod
    def enter():
        print("You do a dive roll into the Weapon Armory, crouch and scan the room")
        print("for more Gothons that might be hiding.  It's dead quiet, too quiet.")
        print("You stand up and run to the far side of the room and find the")
        print("neutron bomb in its container.  There's a keypad lock on the box")
        print("and you need the code to get the bomb out.  If you get the code")
        print("wrong 10 times then the lock closes forever and you can't")
        print("get the bomb.  The code is 3 digits.")
        code = "%d%d%d" % (randint(1, 9), randint(1, 9), randint(1, 9))
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print("BZZZZEDDD!")
            guesses += 1
            guess = input("[keypad]> ")

        if guess == code:
            print("The container clicks open and the seal breaks, letting gas out.")
            print("You grab the neutron bomb and run as fast as you can to the")
            print("bridge where you must place it in the right spot.")
            return 'the_bridge'
        else:
            print("The lock buzzes one last time and then you hear a sickening")
            print("melting sound as the mechanism is fused together.")
            print("You decide to sit there, and finally the Gothons blow up the")
            print("ship from their ship and you die.")
            return 'death'
