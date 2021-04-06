from abc import ABCMeta, abstractmethod


class Scene(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def enter(self):
        """
        Enter method to every scene
        :return:
        """
        pass


class Engine(object):
    __metaclass__ = ABCMeta

    def __init__(self, scene_map):
        self.scene_map = scene_map

    @abstractmethod
    def play(self):
        pass


class Map(object):
    __metaclass__ = ABCMeta

    def __init__(self, start_scene):
        self.start_scene = start_scene

    @abstractmethod
    def next_scene(self, scene_name):
        pass

    @abstractmethod
    def opening_scene(self):
        pass
