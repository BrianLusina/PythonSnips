from abc import ABCMeta, abstractmethod
from sys import exit
from random import randint


class Scene(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def enter(self):
        print("This is not yet implemented, subclass it and run again")
        exit()


class Engine(object):

    __metaclass__ = ABCMeta

    def __init__(self, scene_map):
        self.scene_map = scene_map

    @abstractmethod
    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene("finished")

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()


class Map(object):

    __metaclass__ = ABCMeta

    def __init__(self, start_scene):
        pass

    @abstractmethod
    def next_scene(self, scene_name):
        pass

    @abstractmethod
    def opening_scene(self):
        pass


class EscapePod(Scene):
    def enter(self):
        pass

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()

