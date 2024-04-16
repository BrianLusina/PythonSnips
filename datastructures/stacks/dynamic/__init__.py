from datastructures.stacks import Stack, T


class DynamicSizeStack(Stack):
    """
    Implementation of a Dynamic Size Stack data structure. This can grow or shrink dynamically. If the
    stack is full and an attempt is made to add an element it automatically increases the size of the stack to
    accommodate the new element.
    """

    def __init__(self):
        """
        Creates a new Stack object. Will initialize a stack which will be an empty list
        """
        super().__init__()
        self.stack = []

    def push(self, item: T):
        """
        Storing an element to the top of the stack
        Check if the stack is empty, if it is pushes the element to the stack
        """
        self.stack.append(item)

    def pop(self) -> T:
        """
        Removes an item from the stack, check if the stack is empty, raise an error if it is
        If stack is not empty get the top most item in the stack
        Return:
            T: The top most item in the stack
        Raises:
            Exception if the stack is empty
        """
        if self.is_empty():
            raise Exception("Stack is empty, add item to stack.")
        return self.stack.pop()

    def peek(self) -> T:
        """
        Get the top data element of the stack without removing it
        Check if the stack is empty, if the stack is empty raise an error
        If the stack is full or not empty, return the top most item
        :return: The top data item in the stack
        """

        if self.is_empty():
            raise Exception("Stack is empty, nothing to peek")
        return self.stack[-1]

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
