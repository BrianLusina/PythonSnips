from .. import Stack


class MaxStack(Stack):

    def __init__(self, maxsize: int = None):
        """
        Initializes a Maximum stack with a max size defaulted to None. If set to None, the ma stack has no upper bound
        @param maxsize Maximum size of the stack
        """
        super().__init__(maxsize)
        # keeps track of current minimum of the stack
        self.maximum = float("-inf")

    def push(self, val: int) -> None:
        """
        Pushes an item to the top of the stack
        @param val: Item
        @return: None
        """
        super().push(val)
        if val > self.maximum:
            self.maximum = val

    def pop(self) -> None:
        """
        Removes an item from the top of the stack without returning it
        @return: None
        """
        v = super().pop()
        if len(self.stack) == 0:
            self.maximum = float("-inf")
        elif self.maximum == v:
            self.maximum = max(self.stack)

    def peek(self) -> int:
        """
        Gets the top item from the stack without removing it from the stack
        @return: top item in the stack
        """
        return super().peek()

    def get_max(self) -> int:
        """
        Gets the minimum item from the stack
        @return: minimum item in the stack
        """
        return self.maximum
