"""
MaxStack keeps track of the current maximum value in a Stack data structure.
"""

from typing import TypeVar
from datastructures.stacks.dynamic import DynamicSizeStack, T


class MaxStack(DynamicSizeStack):
    """
    Works exactly like the Stack data structure with the only difference being this keeps track of the current maximum
    value in the Stack. When performing lookups, that is a Peek operation, this will still be an O(1) operation as it
    will return the top most item in the stack. The Pop operation, however, will remove the top item from the
    stack & check if the removed item from the stack is the current maximum value, if it is, then a new maximum value
    has to be checked from the remaining values in the stack and updated appropriately. This is essential to keeping the
    data valid. This causes the worst case Time Complexity to be O(n) where n is the remaining values in the stack as
    iteration has to occur to find the new maximum value.
    """

    def __init__(self):
        """
        Initializes a Maximum stack with a max size defaulted to None. If set to None, the ma stack has no upper bound
        """
        super().__init__()
        # keeps track of current minimum of the stack
        self.maximum = None

    def push(self, val: T) -> None:
        """
        Pushes an item to the top of the stack
        @param val: Item
        @return: None
        """
        super().push(val)
        if self.maximum is not None:
            if val > self.maximum:
                self.maximum = val
        else:
            self.maximum = val

    def pop(self) -> T:
        """
        Removes an item from the top of the stack without returning it
        @return: T
        """
        data = super().pop()
        if len(self.stack) == 0:
            self.maximum = None
        elif self.maximum == data:
            self.maximum = max(self.stack)
        return data

    def peek(self) -> T:
        """
        Gets the top item from the stack without removing it from the stack
        @return: top item in the stack
        """
        return super().peek()

    def get_max(self) -> T:
        """
        Gets the maximum item from the stack
        @return: maximum item in the stack
        """
        return self.maximum
