from collections import deque


class Stack(object):
    """
    Implementation of a Stack data structure
    """
    def __init__(self, max_size):
        """
        Creates a new Stack object. Will initialize a stack which will be an empty list
        :param max_size The maximum size of the stack
        """
        self.stack = deque(maxlen=max_size)

    def push(self, item):
        """
        Storing an element to the top of the stack
        Check if the stack is empty, if it is pushes the element to the stack
        If the stack is full, raises an error
        """
        if self.is_empty():
            self.stack.append(item)
        if self.is_full():
            raise IndexError("Stack is currently full")
        if not self.is_empty() and not self.is_full():
            self.stack.appendleft(item)

    def pop(self, item):
        """
        Removes an item from the stack
        :param item: The item to remove
        :return:
        """
        pass

    def peek(self):
        """
        Get the top data element of the stack without removing it
        Check if the stack is empty, if the stack is empty raise an error
        If the stack is full or not empty, return the top most item
        :return: The top data item in the stack
        """
        if self.is_empty():
            raise IndexError("Stack is empty, nothing to peek")
        return self.stack[0]

    def is_full(self):
        """
        Check if the stack is full
        :return: True Or False
        :rtype: bool
        """
        return len(self.stack) >= self.stack.maxlen

    def is_empty(self):
        """
        Check if the stack is empty
        :return: True or False
        :rtype: bool
        """
        return len(self.stack) == 0

