
"""
Create a class Ghost

Ghost objects are instantiated without any arguments.

Ghost objects are given a random color attribute of white" or "yellow" or "purple" or "red" when instantiated

ghost = Ghost()
ghost.color  #=> "white" or "yellow" or "purple" or "red"
c# Ghost ghost = new Gost(); ghost.GetColor(); // => "white" or "yellow" or "purple" or "red"
"""
import random, math


class Ghost(object):
    @classmethod
    def color(self):
        colors = ["red", "purple", "white", "yellow"]
        return colors[random.randint(0, 3)]


ghost = Ghost
print ghost.color()

