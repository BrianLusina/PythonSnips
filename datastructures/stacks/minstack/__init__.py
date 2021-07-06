from .. import Stack


class MinStack(Stack):

    def __init__(self, maxsize: int = None):
        """
        Initializes a Minimum stack with a max size defaulted to None. If set to None, the min stack has no upper bound
        @param maxsize Maximum size of the stack
        """
        super().__init__(maxsize)
        # keeps track of current minimum of the stack
        self.minimum = float("inf")

    def push(self, val: int) -> None:
        """
        Pushes an item to the top of the stack
        @param val: Item
        @return: None
        """
        super().push(val)
        if val < self.minimum:
            self.minimum = val

    def pop(self) -> None:
        """
        Removes an item from the top of the stack without returning it
        @return: None
        """
        v = super().pop()
        if len(self.stack) == 0:
            self.minimum = float("inf")
        elif self.minimum == v:
            self.minimum = min(self.stack)

    def peek(self) -> int:
        """
        Gets the top item from the stack without removing it from the stack
        @return: top item in the stack
        """
        return super().peek()

    def get_min(self) -> int:
        """
        Gets the minimum item from the stack
        @return: minimum item in the stack
        """
        return self.minimum
