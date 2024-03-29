from abc import ABC, abstractmethod


class Visitor(ABC):
    """
    Visitor interface declares a set of visiting methods that correspond to component classes. The signature of a
    visiting method allows the visitor to identify the exact class of the component that it is dealing with
    """

    @abstractmethod
    def visit_concrete_component_a(self, element):
        pass

    @abstractmethod
    def visit_concrete_component_b(self, element):
        pass
