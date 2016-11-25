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

    # __metaclass__ = ABCMeta

    def __init__(self, scene_map):
        self.scene_map = scene_map

    # @abstractmethod
    # def play(self):
    #     pass

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
        self.start_scene = start_scene

    @abstractmethod
    def next_scene(self, scene_name):
        pass

    @abstractmethod
    def opening_scene(self):
        pass

