import random


class Ghost:
    @classmethod
    def color(cls):
        colors = ["red", "purple", "white", "yellow"]
        return colors[random.randint(0, 3)]


ghost = Ghost
print(ghost.color())
