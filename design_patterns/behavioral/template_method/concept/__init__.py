from abstract_class import AbstractClass
from concrete_class_1 import ConcreteClass1
from concrete_class_2 import ConcreteClass2


def client(abstract: AbstractClass) -> None:
    """
    The client code calls the template method to execute the algorithm. Client
    code does not have to know the concrete class of an object it works with, as
    long as it works with objects through the interface of their base class.
    """
    abstract.template_method()


if __name__ == "__main__":
    print("Same client code can work with different subclasses:")
    client(ConcreteClass1())
    print("")

    print("Same client code can work with different subclasses:")
    client(ConcreteClass2())
