"""
Concrete Visitors implement several versions of the same algorithm, which can
work with all concrete component classes.

You can experience the biggest benefit of the Visitor pattern when using it with
a complex object structure, such as a Composite tree. In this case, it might be
helpful to store some intermediate state of the algorithm while executing
visitor's methods over various objects of the structure.
"""

from visitor import Visitor
from concrete_component_a import ConcreteComponentA
from concrete_component_b import ConcreteComponentB


class ConcreteVisitor1(Visitor):
    def visit_concrete_component_a(self, element: ConcreteComponentA):
        print(
            f"{element.exclusive_method_of_concreate_component_a()} + ConcreteVisitor1"
        )

    def visit_concrete_component_b(self, element: ConcreteComponentB):
        print(f"{element.special_method_of_concreate_component_b()} + ConcreteVisitor1")
