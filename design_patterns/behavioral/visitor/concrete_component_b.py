from component import Component


class ConcreteComponentB(Component):
    """
    Each concrete component must implement the 'accept' method in such a way that it calls the visitor's method
    corresponding to the component class
    """

    def accept(self, visitor):
        visitor.visit_concrete_component_b(self)

    def special_method_of_concreate_component_b(self) -> str:
        """
        Concrete Components may have special methods that don't exist in their
        base class or interface. The Visitor is still able to use these methods
        since it's aware of the component's concrete class.
        @return:
        """
        return "B"
