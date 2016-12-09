import random


class Ghost(object):
    @classmethod
    def color(self):
        colors = ["red", "purple", "white", "yellow"]
        return colors[random.randint(0, 3)]


ghost = Ghost
print(ghost.color())
