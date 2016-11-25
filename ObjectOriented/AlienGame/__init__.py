from abc import ABCMeta, abstractmethod


class Scene(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def enter(self):
        pass


class Engine(object):

    __metaclass__ = ABCMeta

    def __init__(self, scene_map):
        pass

    @abstractmethod
    def play(self):
        pass


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


class Death(Scene):
    def enter(self):
        pass


class CentralCorridor(Scene):
    def enter(self):
        pass


class TheBridge(Scene):
    def enter(self):
        pass


class EscapePod(Scene):
    def enter(self):
        pass


class LaserWeaponArmory(Scene):
    def enter(self):
        pass

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()

