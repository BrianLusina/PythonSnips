from random import sample
from string import ascii_letters
from memento import Memento
from concrete_memento import ConcreteMemento


def _generate_random_string(length: int = 10) -> str:
    return "".join(sample(ascii_letters, length))


class Originator:
    """
    The originator holds some important state that may change over time. It also defines a method for saving the state
    inside a mememnto and another method for restoring state from it
    """

    """
    For the sake of simplicity, the originator's state is stored inside a single variable
    """
    _state = None

    def __init__(self, state: str) -> None:
        self._state = state
        print(f"Originator: My initial state is: {self._state}")

    def do_something(self) -> None:
        """
        The originator's business logic may affect its internal state. Therefore, the client should backup the state
        before launching methods of the business logic via save() method
        """
        print("Originator: I am doing something very important")
        self._state = _generate_random_string(30)
        print(f"Originator: and my state has changed to {self._state}")

    def save(self) -> Memento:
        """Saves the current state inside a memento and returns it"""
        return ConcreteMemento(self._state)

    def restore(self, memento: Memento) -> None:
        """Restores originators state from memento"""
        self._state = memento.get_state()
        print(f"Originator: My state has changed to: {self._state}")
