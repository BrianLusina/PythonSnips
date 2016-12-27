from collections import deque


class Stack(object):
    """
    Implementation of a Stack data structure
    """

    def __init__(self, max_size):
        """
        Creates a new Stack object. Will initialize a stack which will be an empty list
        :param max_size The maximum size of the stack
        self.max_stack will store the maximum in the stack, only does this for numeric values
        We use max_stack to keep our max up to date in constant time as we push() and pop():
        The same applies for min_stack
        """
        self.stack = deque(maxlen=max_size)
        self.max_stack = deque(maxlen=max_size)
        self.min_stack = deque(maxlen=max_size)

    def push(self, item):
        """
        Storing an element to the top of the stack
        Check if the stack is empty, if it is pushes the element to the stack
        This will also keep upto date with the maximum value in the stack
        If the stack is full, raises an error
        """
        if self.is_full():
            raise OverflowError("Stack is currently full")
        if self.is_empty():
            self.stack.append(item)
        elif not self.is_empty() and not self.is_full():
            self.stack.append(item)
            # check if the all the items are numeric integers/floats
            if self.max_stack.peek() is None or item >= self.max_stack.peek():
                self.max_stack.push(item)

    def pop(self):
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

    def peek(self):
        """
        Get the top data element of the stack without removing it
        Check if the stack is empty, if the stack is empty raise an error
        If the stack is full or not empty, return the top most item
        :return: The top data item in the stack
        """

        if self.is_empty():
            raise Exception("Stack is empty, nothing to peek")
        return self.stack[-1]

    def is_full(self):
        """
        Check if the stack is full
        :return: True Or False
        :rtype: bool
        """
        return len(self.stack) == self.stack.maxlen

    def is_empty(self):
        """
        Check if the stack is empty
        :return: True or False
        :rtype: bool
        """
        return len(self.stack) == 0

    def get_len(self):
        """
        Gets the current length of the stack
        :return: The length of the stack
        """
        return len(self.stack)

    def get_max(self) -> int or float:
        """
        Gets the maximum value in a Stack
        :return: the maximum in a Stack
        :rtype: int
        :rtype: float
        """
        return max(self.stack)

    def get_min(self) -> int or float:
        """
        Gets the minumum value in the stack
        :return: The minimum item in the stack
        :rtype: int
        :rtype: float
        """
        return min(self.stack)

    def __len__(self):
        return self.stack.maxlen

    def __str__(self):
        return "{}".format(self.stack)
