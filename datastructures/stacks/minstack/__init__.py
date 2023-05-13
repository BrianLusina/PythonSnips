"""
Contains MinStack data structure that is used to keep track of the current minimum value in a Stack data structure.
All operations pertaining to a Stack data structure remain true for the MinStack.

Complexity analysis varies when performing Pop operations(removing the current top item from the stack). This is because
a new minimum has to be iterated over the current items in the stack in order to keep track of the new minimum value.
This will be an O(n) operation as the Pop() function has to iterate over the remaining items in the worst case.
"""
from typing import TypeVar
from .. import Stack

T = TypeVar("T")


class MinStack(Stack):
    def __init__(self, maxsize: int = None):
        """
        Initializes a Minimum stack with a max size defaulted to None. If set to None, the min stack has no upper bound
        @param maxsize Maximum size of the stack
        """
        super().__init__(maxsize)
        # keeps track of current minimum of the stack
        self.minimum = None

    def push(self, val: int) -> None:
        """
        Pushes an item to the top of the stack
        @param val: Item
        @return: None
        """
        super().push(val)
        if self.minimum is not None:
            if val < self.minimum:
                self.minimum = val
        else:
            self.minimum = val

    def pop(self) -> T:
        """
        Removes an item from the top of the stack without returning it
        @return: None
        """
        data = super().pop()
        if len(self.stack) == 0:
            self.minimum = None
        elif self.minimum == data:
            self.minimum = min(self.stack)
        return data

    def peek(self) -> T:
        """
        Gets the top item from the stack without removing it from the stack
        @return: top item in the stack
        """
        return super().peek()

    def get_min(self) -> T:
        """
        Gets the minimum item from the stack
        @return: minimum item in the stack
        """
        return self.minimum
