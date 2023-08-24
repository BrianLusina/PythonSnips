from abc import ABCMeta, abstractmethod


class Shape:
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def area(self):
        pass
