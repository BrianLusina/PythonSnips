from typing import List
from component import Component
from concrete_component_a import ConcreteComponentA
from concrete_component_b import ConcreteComponentB
from concrete_visitor_1 import ConcreteVisitor1
from concrete_visitor_2 import ConcreteVisitor2
from visitor import Visitor


def client(components: List[Component], guest: Visitor) -> None:
    for c in components:
        c.accept(guest)


if __name__ == "__main__":
    components = [ConcreteComponentA(), ConcreteComponentB()]

    print("The client works with all visitors via the base interface")
    visitor1 = ConcreteVisitor1()
    client(components, visitor1)

    print("It allows the same client to work with different types of visitors")
    visitor2 = ConcreteVisitor2()
    client(components, visitor2)
