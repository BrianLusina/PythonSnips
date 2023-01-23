from abc import abstractmethod, ABC
from visitor import Visitor


class Component(ABC):
    """
    Component interface declares an 'accept' method that should take the base visitor interface as an argument
    """

    @abstractmethod
    def accept(self, visitor: Visitor):
        pass
