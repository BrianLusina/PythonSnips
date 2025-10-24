from abc import ABCMeta, abstractmethod, ABC
from typing import TypeVar

T = TypeVar("T")


class Stack(ABC):
    """
    Generic Abstract Stack data structure
    """

    __metaclass__ = ABCMeta

    @abstractmethod
    def push(self, item: T):
        """
        Storing an element to the top of the stack
        Args:
            item(T): item to add to the stack
        """
        raise NotImplementedError("not implemented")

    @abstractmethod
    def pop(self) -> T:
        """
        Removes an item from the stack.
        Returns:
            T: The top most item in the stack
        """
        raise NotImplementedError("not implemented")

    @abstractmethod
    def peek(self) -> T:
        """
        Get the top data element of the stack without removing it
        Returns:
            T: The top most item in the stack without removing it from the stack
        """
        raise NotImplementedError("not implemented")

    @abstractmethod
    def is_empty(self) -> bool:
        """
        Check if the stack is empty
        Returns:
            bool: True or False
        """
        raise NotImplementedError("not implemented")
