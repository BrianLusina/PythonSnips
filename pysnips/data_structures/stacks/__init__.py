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
            # filter all the integers and floats from the stack
            # if self.max_stack.peek() is None or item >= self.max_stack.peek():
            # self.max_stack.push(item)

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

    def filter_stack(self):
        """
        Filters the stack and stores the items into respective groups by data types
        :return: a dictionary with the keys as data types and values as a list of the items in the stack belonging
        to the group
        :rtype: dict
        """
        output = {}
        if self.is_empty():
            return None
        for item in self.stack:
            output[type(item)] = item
        return output

    def display(self):
        """
        Displays the whole stack
        :return: None
        """
        # todo: add top and bottom markers
        print(self.stack)

    def __len__(self):
        return self.stack.maxlen

    def __str__(self):
        return "{}".format(self.stack)


"""Complexity O(1)O(1) time for push(), pop(), and get_max(). O(m)O(m) additional space, where mm is the number of
operations performed on the stack.

Notice that our time-efficient approach takes some additional space, while a lazy ↴ approach (simply walking through
the stack to find the max integer whenever get_max() is called) took no additional space. We've traded some space
efficiency for time efficiency.

  class MaxStack:

    def __init__(self):
        self.stack      = Stack()
        self.maxs_stack = Stack()

    # Add a new item to the top of our stack. If the item is greater
    # than or equal to the last item in maxs_stack, it's
    # the new max! So we'll add it to maxs_stack.
    def push(self, item):
        self.stack.push(item)
        if self.maxs_stack.peek() is None or item >= self.maxs_stack.peek():
            self.maxs_stack.push(item)

    # Remove and return the top item from our stack. If it equals
    # the top item in maxs_stack, they must have been pushed in together.
    # So we'll pop it out of maxs_stack too.
    def pop(self):
        item = self.stack.pop()
        if item == self.maxs_stack.peek():
            self.maxs_stack.pop()
        return item

    # The last item in maxs_stack is the max item in our stack.
    def get_max(self):
        return self.maxs_stack.peek()
"""