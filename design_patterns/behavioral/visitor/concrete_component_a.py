from component import Component
from visitor import Visitor


class ConcreteComponentA(Component):
    """
    Each concrete component must implement the 'accept' method in such a way that it calls the visitor's method
    corresponding to the component class
    """

    def accept(self, visitor: Visitor):
        visitor.visit_concrete_component_a(self)

    def exclusive_method_of_concreate_component_a(self) -> str:
        """
        Concrete Components may have special methods that don't exist in their
        base class or interface. The Visitor is still able to use these methods
        since it's aware of the component's concrete class.
        @return:
        """
        return "A"
