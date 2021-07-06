from collections import deque
from typing import Any

# python 2.x import sanity check
try:
    from Queue import LifoQueue
except ImportError:
    from queue import LifoQueue


class Stack(LifoQueue):
    """
    Implementation of a Stack data structure
    """

    def __init__(self, max_size: int = None):
        """
        Creates a new Stack object. Will initialize a stack which will be an empty list
        :param max_size The maximum size of the stack
        self.max_stack will store the maximum in the stack, only does this for numeric values
        We use max_stack to keep our max up to date in constant time as we push() and pop():
        The same applies for min_stack
        """
        super(Stack, self).__init__()
        self.stack = deque(maxlen=max_size)

    def push(self, item: Any):
        """
        Storing an element to the top of the stack
        Check if the stack is empty, if it is pushes the element to the stack
        This will also keep up to date with the maximum value in the stack
        If the stack is full, raises an error
        """
        if self.is_full():
            raise OverflowError("Stack is currently full")
        if self.is_empty():
            self.stack.append(item)
        elif not self.is_empty() and not self.is_full():
            self.stack.append(item)

    def pop(self) -> Any:
        """
        Removes an item from the stack, check if the stack is empty, raise an error if it is
        If stack is not empty get the top most item in the stack and store it in a variable
        Remove the item from the stack and reduce the length of the stack
        :return: The top most item in the stack
        :rtype: Stack object
        """
        if self.is_empty():
            raise IndexError("Stack is empty, add item to stack.")
        return self.stack.pop()

    def peek(self) -> Any:
        """
        Get the top data element of the stack without removing it
        Check if the stack is empty, if the stack is empty raise an error
        If the stack is full or not empty, return the top most item
        :return: The top data item in the stack
        """

        if self.is_empty():
            raise Exception("Stack is empty, nothing to peek")
        return self.stack[-1]

    def is_full(self) -> bool:
        """
        Check if the stack is full
        :return: True Or False
        :rtype: bool
        """
        return len(self.stack) == self.stack.maxlen

    def is_empty(self) -> bool:
        """
        Check if the stack is empty
        :return: True or False
        :rtype: bool
        """
        return len(self.stack) == 0

    def __len__(self) -> int:
        return len(self.stack)

    def __str__(self) -> str:
        return "{}".format(self.stack)
